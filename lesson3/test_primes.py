import unittest
from primes import eratosthenes, get_primes, get_primes_odd
import pytest


class PrimesTestCase(unittest.TestCase):
    def test_eratosthenes_zero(self):
        result = eratosthenes(0)
        self.assertEqual(result, [])

    def test_eratosthenes_small_number(self):
        result = eratosthenes(10)
        self.assertEqual(result, [2, 3, 5, 7])

    def test_eratosthenes_large_number(self):
        result = eratosthenes(100)
        self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

    def test_get_primes(self):
        result = get_primes(100)
        self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

    def test_get_primes_odd(self):
        result = get_primes_odd(100)
        self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

    # @pytest.mark.timeout(600)
    def test_time_fill_files(self):
        import os
        import time
        test_files_dir = "./tests/5.Primes"
        for filename in sorted(os.listdir(test_files_dir), key=lambda x: int(x.split(".")[1])):
            if filename.endswith(".in"):
                input_file = os.path.join(test_files_dir, filename)
                output_file = os.path.join(test_files_dir, filename.replace(".in", ".out"))
                with open(input_file, "r") as f:
                    up_to_number = int(f.readline().strip())
                with open(output_file, "r") as f:
                    print(f"Open file: {output_file}")
                    expected_value = float(f.readline().strip())
                print(f"calculate primes up to {up_to_number}")
                start_time = time.time()
                result = float(len(get_primes_odd(up_to_number)))
                end_time = time.time()
                actual_time = end_time - start_time
                self.assertEqual(result, expected_value)
                print(f"Expected value: {expected_value}")
                print(f"Actual value: {result}")
                print(f"Actual time: {actual_time}\n")


if __name__ == '__main__':
    unittest.main()
