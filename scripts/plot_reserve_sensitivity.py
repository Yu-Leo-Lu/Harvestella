"""Reserve-Plot Sensitivity Analysis & Plotting for Harvestella Crop Optimizer.

Sweeps reserved plot counts across one or more seasons using the Day-to-Day
MILP solver in `scripts.crop_solver` and plots Season Net Profit vs. Reserved
Plots. Designed for reuse both as an importable Python module and as a CLI tool.

Example CLI usage:
    python scripts/plot_reserve_sensitivity.py
    python scripts/plot_reserve_sensitivity.py --min-reserve 0 --max-reserve 250 --step 5
    python scripts/plot_reserve_sensitivity.py --farm-level 8 --wallet 200000 --mode facets
"""

from __future__ import annotations

import argparse
import csv
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Iterable, Sequence

import matplotlib
import matplotlib.ticker as mticker
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import yaml

# Allow running directly as `python scripts/plot_reserve_sensitivity.py`
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from scripts.crop_solver import OptimizationResult, solve_allocation

ALL_SEASONS: tuple[str, ...] = ("spring", "summer", "fall", "winter")
VALID_PLOT_MODES: tuple[str, ...] = ("dual", "delta", "facets", "absolute")

DEFAULT_UNLOCKED_TOWNS: dict[str, bool] = {
    "Lethe": True,
    "Nemea": True,
    "Shatolla": True,
    "Argene": True,
    "Abandoned Eden": True,
}

SEASON_STYLES: dict[str, dict[str, str]] = {
    "spring": {"label": "Spring", "color": "#2e9f5e", "marker": "o"},
    "summer": {"label": "Summer", "color": "#e07b24", "marker": "s"},
    "fall": {"label": "Fall", "color": "#c0392b", "marker": "^"},
    "winter": {"label": "Winter", "color": "#2980b9", "marker": "D"},
}


# ==============================================================================
# Scenario Builder & Solver Wrapper
# ==============================================================================

def build_season_config(
    season: str,
    *,
    farm_level: int = 9,
    wallet_gold: float = 300_000,
    current_day: int = 1,
    reserve_farm: int = 0,
    reserve_waterside: int = 0,
    reserve_cave: int = 0,
    waterside_plots: int | None = None,
    cave_plots: int | None = None,
    unlocked_towns: dict[str, bool] | None = None,
    max_crop_varieties: int | None = None,
    base_config: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a clean, reproducible season configuration dictionary.

    By default creates a fresh Day 1 scenario using full catalog vendor stock
    from `seasons/<season>.csv`. If `base_config` is provided, its values are
    used as defaults before applying the explicit keyword overrides.
    """
    season_key = season.strip().lower()
    is_winter = season_key == "winter"

    cfg: dict[str, Any] = dict(base_config) if base_config else {}
    cfg["season"] = season_key
    cfg["current_day"] = current_day
    cfg["wallet_gold"] = wallet_gold
    cfg["max_crop_varieties"] = max_crop_varieties
    cfg["farm_level"] = farm_level
    cfg["waterside_plots"] = (
        (0 if is_winter else 81) if waterside_plots is None else waterside_plots
    )
    cfg["cave_plots"] = (
        (0 if is_winter else 81) if cave_plots is None else cave_plots
    )
    cfg["reserve_plots"] = {
        "farm": int(reserve_farm),
        "waterside": int(reserve_waterside),
        "cave": int(reserve_cave),
    }

    if base_config is None:
        cfg["planted"] = []
        cfg["seed_stock"] = {}

    towns = dict(DEFAULT_UNLOCKED_TOWNS)
    if unlocked_towns:
        towns.update(unlocked_towns)
    cfg["unlocked_towns"] = towns
    return cfg


def solve_config_dict(
    cfg: dict[str, Any],
    csv_dir: Path = _REPO_ROOT / "seasons",
) -> OptimizationResult:
    """Run `solve_allocation` on an in-memory config dict via a temp YAML file."""
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".yaml",
        delete=False,
        encoding="utf-8",
    ) as tmp:
        yaml.safe_dump(cfg, tmp, sort_keys=False)
        tmp_path = Path(tmp.name)

    try:
        return solve_allocation(tmp_path, csv_dir=csv_dir)
    finally:
        tmp_path.unlink(missing_ok=True)


# ==============================================================================
# Sensitivity Sweep
# ==============================================================================

def sweep_reserve_plots(
    reserve_values: Iterable[int],
    *,
    seasons: Sequence[str] = ALL_SEASONS,
    biome: str = "farm",
    farm_level: int = 9,
    wallet_gold: float = 300_000,
    current_day: int = 1,
    reserve_farm: int = 0,
    reserve_waterside: int = 0,
    reserve_cave: int = 0,
    unlocked_towns: dict[str, bool] | None = None,
    max_crop_varieties: int | None = None,
    csv_dir: Path = _REPO_ROOT / "seasons",
    max_workers: int | None = None,
) -> dict[str, list[dict[str, Any]]]:
    """Sweep reserved plots for the chosen biome across one or more seasons.

    Args:
        reserve_values: Sequence/iterable of reserved plot counts to evaluate.
        seasons: Season names to evaluate (default: all four seasons).
        biome: Which biome's reserved plot count to sweep (`farm`, `waterside`, or `cave`).
        farm_level: Renovator farm level (49 plots per level).
        wallet_gold: Starting morning wallet on `current_day`.
        current_day: Starting day of the season (1-30).
        reserve_farm: Fixed farm reserve when sweeping another biome.
        reserve_waterside: Fixed waterside reserve when sweeping another biome.
        reserve_cave: Fixed cave reserve when sweeping another biome.
        unlocked_towns: Town unlock flags (defaults to Lethe-Argene unlocked).
        max_crop_varieties: Optional cap on distinct crop varieties.
        csv_dir: Directory containing seasonal crop CSV files.
        max_workers: Thread pool size for concurrent MILP solves.

    Returns:
        Mapping `{season: [{"reserve_plots": ..., "usable_plots": ...,
        "net_profit": ..., "final_wallet": ...}, ...]}` sorted by `reserve_plots`.
    """
    biome_key = biome.strip().lower()
    if biome_key not in {"farm", "waterside", "cave"}:
        raise ValueError(f"Unsupported biome '{biome}'. Choose from 'farm', 'waterside', 'cave'.")

    r_list = sorted(set(int(r) for r in reserve_values))
    season_list = [s.strip().lower() for s in seasons]

    jobs: list[tuple[str, int]] = [(s, r) for s in season_list for r in r_list]

    def _run_job(job: tuple[str, int]) -> tuple[str, dict[str, Any]]:
        season_name, r_val = job
        rf = r_val if biome_key == "farm" else reserve_farm
        rw = r_val if biome_key == "waterside" else reserve_waterside
        rc = r_val if biome_key == "cave" else reserve_cave

        cfg = build_season_config(
            season_name,
            farm_level=farm_level,
            wallet_gold=wallet_gold,
            current_day=current_day,
            reserve_farm=rf,
            reserve_waterside=rw,
            reserve_cave=rc,
            unlocked_towns=unlocked_towns,
            max_crop_varieties=max_crop_varieties,
        )
        res = solve_config_dict(cfg, csv_dir=csv_dir)
        if not res.success:
            raise RuntimeError(f"Solver failed for {season_name} (reserve={r_val}): {res.status_message}")

        usable = (
            res.base_farm
            if biome_key == "farm"
            else res.base_water
            if biome_key == "waterside"
            else res.base_cave
        )
        return season_name, {
            "reserve_plots": r_val,
            "usable_plots": usable,
            "net_profit": float(res.total_season_profit),
            "final_wallet": float(res.final_wallet_gold),
        }

    results: dict[str, list[dict[str, Any]]] = {s: [] for s in season_list}
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        for season_name, row in pool.map(_run_job, jobs):
            results[season_name].append(row)

    for s in season_list:
        results[s].sort(key=lambda item: item["reserve_plots"])

    return results


# ==============================================================================
# Plotting & Export
# ==============================================================================

def save_sweep_csv(
    sweep_data: dict[str, list[dict[str, Any]]],
    csv_path: Path,
) -> Path:
    """Export sweep results to a flat CSV file."""
    csv_path = Path(csv_path)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["season", "reserve_plots", "usable_plots", "net_profit", "final_wallet"])
        for season_name, rows in sweep_data.items():
            for row in rows:
                writer.writerow([
                    season_name,
                    row["reserve_plots"],
                    row["usable_plots"],
                    int(round(row["net_profit"])),
                    int(round(row["final_wallet"])),
                ])
    return csv_path


def _create_figure(
    nrows: int,
    ncols: int,
    *,
    figsize: tuple[float, float],
    sharex: bool = False,
    gridspec_kw: dict[str, Any] | None = None,
    show: bool = False,
) -> tuple[Figure, Any]:
    """Create a Matplotlib Figure with subplots using Agg unless `show=True`."""
    if show:
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(
            nrows,
            ncols,
            figsize=figsize,
            dpi=160,
            sharex=sharex,
            gridspec_kw=gridspec_kw,
        )
        return fig, axes

    fig = Figure(figsize=figsize, dpi=160)
    FigureCanvasAgg(fig)
    axes = fig.subplots(
        nrows,
        ncols,
        sharex=sharex,
        gridspec_kw=gridspec_kw,
    )
    return fig, axes


def _add_reference_lines(
    ax: Any,
    highlight_reserves: Sequence[int],
    x_min: int,
    x_max: int,
    *,
    label_lines: bool = True,
) -> None:
    """Draw vertical dashed reference lines at highlighted reserved plot counts."""
    for ref_x in highlight_reserves:
        if x_min <= ref_x <= x_max:
            ax.axvline(
                ref_x,
                color="#7f8c8d",
                linestyle="--",
                linewidth=1.0,
                alpha=0.65,
                zorder=1,
            )
            if label_lines:
                near_right = ref_x >= x_max - max(2, int((x_max - x_min) * 0.06))
                ax.text(
                    ref_x,
                    0.02,
                    f"{'r=' + str(ref_x) + ' ' if near_right else ' r=' + str(ref_x)}",
                    transform=ax.get_xaxis_transform(),
                    fontsize=8.5,
                    color="#555555",
                    va="bottom",
                    ha="right" if near_right else "left",
                )


def _add_usable_top_axis(ax: Any, physical_plots: int, biome_key: str) -> None:
    """Attach a secondary top x-axis showing usable plots = physical - reserved."""
    ax_top = ax.secondary_xaxis(
        "top",
        functions=(lambda r: physical_plots - r, lambda u: physical_plots - u),
    )
    ax_top.set_xlabel(f"Usable {biome_key.capitalize()} Plots (out of {physical_plots})")


def _format_k_gold(value: float, _pos: Any = None) -> str:
    """Format gold amounts in compact 'k G' units."""
    return f"{value / 1000:,.0f}k G"


def _plot_curves(
    ax: Any,
    active_seasons: list[tuple[str, list[dict[str, Any]]]],
    *,
    use_delta: bool,
    annotate_ends: bool = True,
) -> list[float]:
    """Plot absolute or delta net-profit curves for all active seasons on `ax`."""
    plotted_y: list[float] = []
    for season_name, rows in active_seasons:
        style = SEASON_STYLES.get(
            season_name,
            {"label": season_name.capitalize(), "color": "#555555", "marker": "o"},
        )
        xs = [r["reserve_plots"] for r in rows]
        raw_ys = [r["net_profit"] for r in rows]
        base_y = raw_ys[0]
        ys = [y - base_y for y in raw_ys] if use_delta else raw_ys
        plotted_y.extend(ys)

        delta = raw_ys[-1] - raw_ys[0]
        label = f"{style['label']} (Δ {delta:+,.0f} G)"
        mark_every = max(1, len(xs) // 12)

        ax.plot(
            xs,
            ys,
            label=label,
            color=style["color"],
            linewidth=2.3,
            marker=style["marker"],
            markersize=4.8,
            markevery=mark_every,
        )

        if annotate_ends:
            end_text = f"{ys[-1] / 1000:+.1f}k G" if use_delta else f"{ys[-1] / 1000:.1f}k G"
            ax.annotate(
                end_text,
                xy=(xs[-1], ys[-1]),
                xytext=(6, 0),
                textcoords="offset points",
                va="center",
                fontsize=9.2,
                fontweight="bold",
                color=style["color"],
            )
    return plotted_y


def plot_reserve_sensitivity(
    sweep_data: dict[str, list[dict[str, Any]]],
    *,
    output_path: Path = _REPO_ROOT / "images" / "reserve_plots_sensitivity.png",
    mode: str = "dual",
    biome: str = "farm",
    farm_level: int = 9,
    wallet_gold: float = 300_000,
    current_day: int = 1,
    unlocked_towns: dict[str, bool] | None = None,
    highlight_reserves: Sequence[int] = (60, 133),
    show: bool = False,
) -> Path:
    """Plot Season Net Profit vs. Reserved Plots across all swept seasons.

    Supported `mode` layouts:
      - `dual`: Stacked absolute profit (top) + profit delta vs. r_min (bottom).
      - `delta`: Single panel showing profit change vs. r_min.
      - `facets`: Per-season subplots with a shared y-axis span for 1:1 slope comparison.
      - `absolute`: Single panel showing absolute season net profit.
    """
    mode_key = mode.strip().lower()
    if mode_key not in VALID_PLOT_MODES:
        raise ValueError(f"Unsupported plot mode '{mode}'. Choose from {VALID_PLOT_MODES}.")

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    active_seasons = [(name, rows) for name, rows in sweep_data.items() if rows]
    if not active_seasons:
        raise ValueError("No data points available to plot.")

    all_x = [r["reserve_plots"] for _, rows in active_seasons for r in rows]
    x_min, x_max = min(all_x), max(all_x)
    x_right_pad = max(5, int((x_max - x_min) * 0.12))

    biome_key = biome.strip().lower()
    physical_plots = farm_level * 49 if biome_key == "farm" else 81

    matplotlib.rcParams.update({
        "font.size": 10.2,
        "axes.titlesize": 12.0,
        "axes.labelsize": 10.8,
    })

    towns_cfg = dict(DEFAULT_UNLOCKED_TOWNS)
    if unlocked_towns:
        towns_cfg.update(unlocked_towns)
    eden_tag = "Eden Unlocked" if towns_cfg.get("Abandoned Eden", False) else "Eden Locked"
    subtitle = (
        f"Farm Lv.{farm_level} ({farm_level * 49} plots)  |  "
        f"Day {current_day} Wallet: {wallet_gold:,.0f} G  |  {eden_tag}"
    )

    if mode_key == "dual":
        fig, (ax_abs, ax_delta) = _create_figure(
            2,
            1,
            figsize=(10.5, 8.2),
            sharex=True,
            gridspec_kw={"height_ratios": [1.0, 1.15], "hspace": 0.14},
            show=show,
        )

        abs_y = _plot_curves(ax_abs, active_seasons, use_delta=False)
        abs_pad = max(15_000, (max(abs_y) - min(abs_y)) * 0.08)
        ax_abs.set_ylim(max(0, min(abs_y) - abs_pad), max(abs_y) + abs_pad)
        ax_abs.set_ylabel("Season Net Profit (G)")
        ax_abs.yaxis.set_major_formatter(mticker.FuncFormatter(_format_k_gold))
        ax_abs.grid(True, linestyle=":", alpha=0.55)
        _add_reference_lines(ax_abs, highlight_reserves, x_min, x_max, label_lines=False)
        _add_usable_top_axis(ax_abs, physical_plots, biome_key)

        delta_y = _plot_curves(ax_delta, active_seasons, use_delta=True)
        delta_span = max(delta_y) - min(delta_y)
        delta_pad = max(4_000, delta_span * 0.12)
        ax_delta.axhline(0, color="#34495e", linewidth=1.0, alpha=0.55, zorder=1)
        ax_delta.set_ylim(min(delta_y) - delta_pad, max(delta_y) + delta_pad * 0.6)
        ax_delta.set_ylabel(f"Profit Δ vs. r={x_min} (G)")
        ax_delta.set_xlabel(f"Reserved {biome_key.capitalize()} Plots")
        ax_delta.set_xlim(x_min - 1, x_max + x_right_pad)
        ax_delta.yaxis.set_major_formatter(mticker.FuncFormatter(_format_k_gold))
        ax_delta.grid(True, linestyle=":", alpha=0.55)
        _add_reference_lines(ax_delta, highlight_reserves, x_min, x_max, label_lines=True)

        handles, labels = ax_delta.get_legend_handles_labels()
        fig.legend(
            handles,
            labels,
            loc="lower center",
            bbox_to_anchor=(0.5, 0.01),
            ncol=2,
            frameon=True,
            framealpha=0.95,
        )
        fig.suptitle(
            f"Harvestella Season Net Profit vs. Reserved {biome_key.capitalize()} Plots",
            fontsize=13.5,
            fontweight="bold",
            y=0.985,
        )
        fig.text(0.5, 0.945, subtitle, ha="center", va="center", fontsize=9.8, color="#555555")
        fig.subplots_adjust(top=0.86, bottom=0.14, left=0.10, right=0.95)

    elif mode_key in {"absolute", "delta"}:
        use_delta = mode_key == "delta"
        fig, ax = _create_figure(1, 1, figsize=(10.5, 6.2), show=show)
        plotted_y = _plot_curves(ax, active_seasons, use_delta=use_delta)

        if use_delta:
            span = max(plotted_y) - min(plotted_y)
            y_pad = max(4_000, span * 0.12)
            ax.axhline(0, color="#34495e", linewidth=1.0, alpha=0.55, zorder=1)
            ax.set_ylim(min(plotted_y) - y_pad, max(plotted_y) + y_pad * 0.6)
            ax.set_ylabel(f"Profit Δ vs. r={x_min} (G)")
            title_metric = "Net Profit Change"
        else:
            y_pad = max(15_000, (max(plotted_y) - min(plotted_y)) * 0.08)
            ax.set_ylim(max(0, min(plotted_y) - y_pad), max(plotted_y) + y_pad)
            ax.set_ylabel("Season Net Profit (G)")
            title_metric = "Season Net Profit"

        _add_reference_lines(ax, highlight_reserves, x_min, x_max, label_lines=True)
        _add_usable_top_axis(ax, physical_plots, biome_key)

        ax.set_xlabel(f"Reserved {biome_key.capitalize()} Plots")
        ax.set_xlim(x_min - 1, x_max + x_right_pad)
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(_format_k_gold))
        ax.grid(True, linestyle=":", alpha=0.55)
        ax.legend(
            loc="upper center",
            bbox_to_anchor=(0.5, -0.13),
            ncol=2,
            frameon=True,
            framealpha=0.95,
        )
        fig.suptitle(
            f"Harvestella {title_metric} vs. Reserved {biome_key.capitalize()} Plots",
            fontsize=13.5,
            fontweight="bold",
            y=0.985,
        )
        fig.text(0.5, 0.935, subtitle, ha="center", va="center", fontsize=9.8, color="#555555")
        fig.tight_layout(rect=(0, 0.05, 1, 0.91))

    else:
        # "facets": shared y-axis height across subplots so slopes are 1:1 comparable
        n_panels = len(active_seasons)
        ncols = 1 if n_panels == 1 else 2
        nrows = (n_panels + ncols - 1) // ncols
        fig, axes = _create_figure(
            nrows,
            ncols,
            figsize=(11.2, 4.1 * nrows + 1.0),
            sharex=True,
            show=show,
        )
        flat_axes = list(axes.flat) if hasattr(axes, "flat") else [axes]

        season_spans = [
            max(r["net_profit"] for r in rows) - min(r["net_profit"] for r in rows)
            for _, rows in active_seasons
        ]
        shared_height = max(20_000.0, max(season_spans) * 1.25)

        for idx, (season_name, rows) in enumerate(active_seasons):
            ax = flat_axes[idx]
            style = SEASON_STYLES.get(
                season_name,
                {"label": season_name.capitalize(), "color": "#555555", "marker": "o"},
            )
            xs = [r["reserve_plots"] for r in rows]
            ys = [r["net_profit"] for r in rows]
            delta = ys[-1] - ys[0]
            mid_y = 0.5 * (min(ys) + max(ys))
            y_lo = max(0.0, mid_y - shared_height / 2.0)
            y_hi = y_lo + shared_height

            mark_every = max(1, len(xs) // 10)
            ax.plot(
                xs,
                ys,
                color=style["color"],
                linewidth=2.3,
                marker=style["marker"],
                markersize=4.8,
                markevery=mark_every,
            )
            ax.set_ylim(y_lo, y_hi)
            ax.set_xlim(x_min - 1, x_max + 2)
            ax.set_title(
                f"{style['label']}  (Δ {delta:+,.0f} G)",
                fontweight="bold",
                color=style["color"],
                pad=8,
            )
            ax.yaxis.set_major_formatter(mticker.FuncFormatter(_format_k_gold))
            ax.grid(True, linestyle=":", alpha=0.55)
            _add_reference_lines(ax, highlight_reserves, x_min, x_max, label_lines=(idx >= n_panels - ncols))

            if idx % ncols == 0:
                ax.set_ylabel("Season Net Profit (G)")
            if idx >= n_panels - ncols:
                ax.set_xlabel(f"Reserved {biome_key.capitalize()} Plots")
            if idx < ncols:
                _add_usable_top_axis(ax, physical_plots, biome_key)

        for extra_ax in flat_axes[n_panels:]:
            extra_ax.set_visible(False)

        fig.suptitle(
            f"Harvestella Season Net Profit vs. Reserved {biome_key.capitalize()} Plots (Matched Scale)",
            fontsize=13.5,
            fontweight="bold",
            y=0.985,
        )
        fig.text(0.5, 0.942, subtitle, ha="center", va="center", fontsize=9.8, color="#555555")
        fig.tight_layout(rect=(0, 0.01, 1, 0.91))

    fig.savefig(output_path, bbox_inches="tight")
    if show:
        import matplotlib.pyplot as plt
        plt.show()
        plt.close(fig)
    return output_path


# ==============================================================================
# CLI Entry Point
# ==============================================================================

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sweep reserved plot counts and plot Season Net Profit across seasons."
    )
    parser.add_argument("--min-reserve", type=int, default=40, help="Minimum reserved plots (default: 40)")
    parser.add_argument("--max-reserve", type=int, default=133, help="Maximum reserved plots (default: 133)")
    parser.add_argument("--step", type=int, default=1, help="Step size for reserved plots sweep (default: 1)")
    parser.add_argument("--biome", choices=["farm", "waterside", "cave"], default="farm", help="Biome to sweep (default: farm)")
    parser.add_argument("--farm-level", type=int, default=9, help="Renovator farm level (default: 9)")
    parser.add_argument("--wallet", type=float, default=300_000, help="Day 1 starting wallet gold (default: 300000)")
    parser.add_argument("--day", type=int, default=1, help="Starting day of the season (default: 1)")
    parser.add_argument(
        "--seasons",
        nargs="+",
        choices=list(ALL_SEASONS),
        default=list(ALL_SEASONS),
        help="Seasons to include (default: all four)",
    )
    parser.add_argument(
        "--mode",
        choices=list(VALID_PLOT_MODES),
        default="dual",
        help="Chart layout mode: dual (default), delta, facets, or absolute",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=_REPO_ROOT / "images" / "reserve_plots_sensitivity.png",
        help="Output PNG path",
    )
    parser.add_argument("--csv-output", type=Path, default=None, help="Optional path to export sweep data as CSV")
    parser.add_argument("--show", action="store_true", help="Display the plot interactively")
    args = parser.parse_args()

    if args.max_reserve < args.min_reserve:
        raise ValueError("--max-reserve must be >= --min-reserve")
    if args.step <= 0:
        raise ValueError("--step must be a positive integer")

    # Always include exact endpoints so the range boundaries are exact
    reserve_vals = list(range(args.min_reserve, args.max_reserve + 1, args.step))
    if reserve_vals[-1] != args.max_reserve:
        reserve_vals.append(args.max_reserve)

    unlocked = dict(DEFAULT_UNLOCKED_TOWNS)

    print(
        f"Sweeping {args.biome} reserve plots {args.min_reserve}..{args.max_reserve} "
        f"(step={args.step}, {len(reserve_vals)} points x {len(args.seasons)} seasons)..."
    )
    sweep_data = sweep_reserve_plots(
        reserve_vals,
        seasons=args.seasons,
        biome=args.biome,
        farm_level=args.farm_level,
        wallet_gold=args.wallet,
        current_day=args.day,
        unlocked_towns=unlocked,
    )

    if args.csv_output:
        save_sweep_csv(sweep_data, args.csv_output)
        print(f"Saved sweep CSV: {args.csv_output}")

    out_path = plot_reserve_sensitivity(
        sweep_data,
        output_path=args.output,
        mode=args.mode,
        biome=args.biome,
        farm_level=args.farm_level,
        wallet_gold=args.wallet,
        current_day=args.day,
        unlocked_towns=unlocked,
        show=args.show,
    )
    print(f"Saved sensitivity plot: {out_path}\n")

    # Concise terminal summary
    print(f"{'Season':<10} | {'r=' + str(args.min_reserve):>12} | {'r=' + str(args.max_reserve):>12} | {'Delta':>11} | {'G / plot':>9}")
    print("-" * 66)
    span = max(1, args.max_reserve - args.min_reserve)
    for s in args.seasons:
        rows = sweep_data[s]
        p_start = rows[0]["net_profit"]
        p_end = rows[-1]["net_profit"]
        diff = p_end - p_start
        print(f"{s.capitalize():<10} | {p_start:>10,.0f} G | {p_end:>10,.0f} G | {diff:>+9,.0f} G | {abs(diff) / span:>7.1f} G")


if __name__ == "__main__":
    main()
