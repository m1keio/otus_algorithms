import unittest
import pytest
from power import power_memo


class PowerMemoTestCase(unittest.TestCase):
    def test_power_zero(self):
        memo = {}
        self.assertEqual(power_memo(5, 0, memo), 1)

    def test_power_positive(self):
        memo = {}
        self.assertEqual(power_memo(2, 5, memo), 32)

    def test_power_float(self):
        memo = {}
        self.assertEqual(power_memo(1.01, 5, memo), 1.0510100501)

    @pytest.mark.timeout(120)
    def test_time_fill_files(self):
        import os
        import time
        test_files_dir = "./tests/3.Power"
        for filename in sorted(os.listdir(test_files_dir), key=lambda x: int(x.split(".")[1])):
            if filename.endswith(".in"):
                input_file = os.path.join(test_files_dir, filename)
                output_file = os.path.join(test_files_dir, filename.replace(".in", ".out"))
                with open(input_file, "r") as f:
                    base = float(f.readline().strip())
                    power = int(f.readline().strip())
                with open(output_file, "r") as f:
                    print(f"Open file: {output_file}")
                    expected_value = float(f.readline().strip())
                print(f"calculate power: {base} ^ {power}")
                start_time = time.time()
                memo = {}
                result = power_memo(base, power, memo)
                end_time = time.time()
                actual_time = end_time - start_time
                # self.assertEqual(result, expected_value)
                assert expected_value == pytest.approx(result, 0.0001)
                print(f"Expected value: {expected_value}")
                print(f"Actual value: {result}")
                print(f"Actual time: {actual_time}\n")


if __name__ == '__main__':
    unittest.main()
