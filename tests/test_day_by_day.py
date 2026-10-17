"""Test suite for Day-to-Day Time-Indexed Crop Allocation Optimization."""

from pathlib import Path
import unittest

from scripts.crop_solver import solve_allocation


class TestDayByDayOptimization(unittest.TestCase):
    def test_spring_optimization(self):
        res = solve_allocation(Path("configs/spring.yaml"))
        self.assertIsNotNone(res)
        self.assertTrue(res.success, msg=res.status_message)
        self.assertGreater(res.total_season_profit, 0)
        self.assertGreater(len(res.daily_records), 0)

    def test_summer_optimization(self):
        res = solve_allocation(Path("configs/summer.yaml"))
        self.assertIsNotNone(res)
        self.assertTrue(res.success, msg=res.status_message)
        self.assertGreater(res.total_season_profit, 0)
        self.assertGreater(len(res.daily_records), 0)

    def test_fall_optimization(self):
        res = solve_allocation(Path("configs/fall.yaml"))
        self.assertIsNotNone(res)
        self.assertTrue(res.success, msg=res.status_message)
        self.assertGreater(res.total_season_profit, 0)
        self.assertGreater(len(res.daily_records), 0)

    def test_winter_optimization(self):
        res = solve_allocation(Path("configs/winter.yaml"))
        self.assertIsNotNone(res)
        self.assertTrue(res.success, msg=res.status_message)
        self.assertGreater(res.total_season_profit, 0)
        self.assertGreater(len(res.daily_records), 0)


if __name__ == "__main__":
    unittest.main()
