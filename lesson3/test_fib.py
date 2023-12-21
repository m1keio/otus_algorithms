import time
import unittest
from fib import fib, fib_bottom_up


class FibTestCase(unittest.TestCase):
    import sys
    sys.set_int_max_str_digits(0)

    def test_fib_zero(self):
        result = fib(0)
        self.assertEqual(result, 0)

    def test_fib_large_number(self):
        result = fib(10)
        self.assertEqual(result, 55)

    def test_time_fill_files(self):
        import os
        test_files_dir = "./tests/4.Fibo"
        for filename in sorted(os.listdir(test_files_dir), key=lambda x: int(x.split(".")[1])):
            if filename.endswith(".in"):
                input_file = os.path.join(test_files_dir, filename)
                output_file = os.path.join(test_files_dir, filename.replace(".in", ".out"))
                with open(input_file, "r") as f:
                    fib_len = int(f.readline().strip())
                with open(output_file, "r") as f:
                    print(f"Open file: {output_file}")
                    expected_value = int(f.readline().strip())
                print(f"Find fibonacci number : {fib_len}")
                start_time = time.time()
                result = fib_bottom_up(fib_len)
                end_time = time.time()
                actual_time = end_time - start_time
                self.assertEqual(result, expected_value)
                print(f"Expected value: {expected_value}")
                print(f"Actual value: {result}")
                print(f"Actual time: {actual_time}\n")


if __name__ == '__main__':
    unittest.main()
