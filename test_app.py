import unittest
from datetime import datetime

from fastapi import HTTPException

from utils import calculate_avg, calculate_moving_avg


class TestDataFunctions(unittest.TestCase):
    def setUp(self):
        self.datapoints = [
            (
                "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_75b662e3-972c-4611-a9b4-7450dc2b718f",
                datetime(2023, 8, 12, 17, 40, 28, 237504),
                100.0,
            ),
            (
                "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_91e0015e-153c-489f-b088-1077f50be858",
                datetime(2023, 8, 12, 17, 40, 29, 865331),
                200.0,
            ),
            (
                "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_4de8b7ba-43b4-422a-bb5f-7fe78a2c001e",
                datetime(2023, 8, 12, 17, 41, 23, 357955),
                300.0,
            ),
            (
                "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_4de8b7ba-43b4-422a-bb5f-7fe78a2c0011",
                datetime(2023, 8, 13, 9, 41, 23, 357955),
                400.0,
            ),
            (
                "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_4de8b7ba-43b4-422a-bb5f-7fe78a2c0012",
                datetime(2023, 8, 13, 9, 42, 23, 357955),
                500.0,
            ),
            (
                "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_4de8b7ba-43b4-422a-bb5f-7fe78a2c0013",
                datetime(2023, 8, 13, 9, 43, 23, 357955),
                600.0,
            ),
            (
                "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_4de8b7ba-43b4-422a-bb5f-7fe78a2c0014",
                datetime(2023, 8, 13, 10, 43, 23, 357955),
                700.0,
            ),
            (
                "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_4de8b7ba-43b4-422a-bb5f-7fe78a2c0015",
                datetime(2023, 8, 13, 10, 45, 23, 357955),
                800.0,
            ),
            (
                "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_4de8b7ba-43b4-422a-bb5f-7fe78a2c0016",
                datetime(2023, 8, 13, 10, 46, 23, 357955),
                900.0,
            ),
        ]

    def test_calculate_avg_with_given_data(self):
        result_avg_values = calculate_avg(self.datapoints)

        expected_avg_values = [
            200.0,
            500.0,
            800.0,
        ]
        self.assertListEqual(result_avg_values, expected_avg_values)

    def test_calculate_moving_avg_with_given_data(self):
        avg_data = [200.0, 500.0, 800.0, 1000.0]
        window_size = 2

        result_moving_avgs = calculate_moving_avg(avg_data, window_size)

        expected_moving_avgs = [350.0, 650.0, 900.0]
        self.assertListEqual(result_moving_avgs, expected_moving_avgs)

    def test_calculate_moving_avg_with_invalid_window_size(self):
        avg_data = [200.0, 500.0, 800.0, 1000.0]
        invalid_window_size = 5

        with self.assertRaises(HTTPException) as context:
            calculate_moving_avg(avg_data, invalid_window_size)

        self.assertEqual(context.exception.status_code, 400)
        self.assertEqual(context.exception.detail, "Invalid window_size")


if __name__ == "__main__":
    unittest.main()
