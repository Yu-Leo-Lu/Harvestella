# Repository Guidelines & Rules

## 1. Communication & Math Formatting

- **Never use LaTeX math mode in chat responses (`$...$` or `$$...$$`)**:
  The chat interface does not render LaTeX and displays it as broken, raw code (e.g., `$d_{\text{prod}} \le 30 - \text{current_day}$` or `($R \in \{11, 21, 31\}$)`).
- **Use inline code backticks or readable Unicode instead**:
  Format all mathematical relationships, bounds, inequalities, and formulas using clean inline code or standard Unicode characters:
  - ✅ `prod_days <= 30 - current_day`
  - ❌ `$d_{\text{prod}} \le 30 - \text{current_day}$`
  - ✅ `Target day in {11, 21, 31}` or `(Days 11, 21, or 31)`
  - ❌ `$R \in \{11, 21, 31\}$`
  - ✅ `Δ Profit = 50 - 15 = +35 G/d`
  - ❌ `$\Delta \text{Profit} = 50 - 15$`

## 2. Code & Documentation Integrity

- Maintain documentation integrity. Preserve all existing comments and docstrings unrelated to current code changes.
- Provide clickable markdown links for referenced files and code symbols.
- Keep explanations clear, practical, and concise.
