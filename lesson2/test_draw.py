import unittest
from draw import fillTickets


class FillTicketsTestCase(unittest.TestCase):
    def test_default_length(self):
        # Test with default length of 6
        tickets = fillTickets(length=2)
        self.assertEqual(len(tickets), 10000)
        self.assertEqual(tickets[0], [0, 0, 0, 0])
        self.assertEqual(tickets[9999], [9, 9, 9, 9])

    def test_custom_length(self):
        # Test with custom length of 3
        tickets = fillTickets(length=1)
        self.assertEqual(len(tickets), 100)
        self.assertEqual(tickets[0], [0, 0])
        self.assertEqual(tickets[99], [9, 9])

    # test if ticket is lucky sum(left half) == sum(right half)
    def test_is_lucky(self):
        from draw import isLucky
        tickets = fillTickets(length=2)
        self.assertTrue(isLucky(tickets[0]))
        self.assertTrue(isLucky(tickets[9999]))
        self.assertFalse(isLucky([1, 2, 3, 4, 5, 6]))
        self.assertFalse(isLucky([1, 2, 3, 0, 5, 7]))

    def test_fill_regular(self):
        from draw import getAllLuckyTickets
        tickets = fillTickets(length=3)
        sum1 = len((getAllLuckyTickets(tickets)))
        self.assertEqual(sum1, 55252)

    def test_fill_faster(self):
        from draw import fillTicketsFaster, getAllLuckyTickets
        tickets = fillTicketsFaster(length=3)
        sum1 = len((getAllLuckyTickets(tickets)))
        self.assertEqual(sum1, 55252)

    def test_compare_speed(self):
        import time
        from draw import fillTickets, fillTicketsFaster, getAllLuckyTickets
        start = time.time()
        tickets = fillTickets(length=3)
        getAllLuckyTickets(tickets)
        end = time.time()
        regular = end - start
        print("Regular: ", regular)

        start_faster = time.time()
        tickets_faster = fillTicketsFaster(length=3)
        getAllLuckyTickets(tickets_faster)
        end_faster = time.time()
        faster = end_faster - start_faster
        print("Faster: ", faster)
        self.assertLess(faster, regular)

    # get length of tickets from files in test/1.Ticktes/test.*.in and compare time of execution for getAllLuckyTickets with number in files test.*.out
    def test_time_fill_files(self):
        import os
        import time
        from draw import fillTickets, getAllLuckyTickets
        test_files_dir = "lesson2/tests/1.Tickets"
        for filename in sorted(os.listdir(test_files_dir)):
            if filename.endswith(".in"):
                input_file = os.path.join(test_files_dir, filename)
                output_file = os.path.join(test_files_dir, filename.replace(".in", ".out"))

                with open(input_file, "r") as f:
                    tickets_length = int(f.readline().strip())

                print(f"Ticket lenght: {tickets_length}")
                start = time.time()
                tickets = fillTickets(length=tickets_length)
                lucky_tickets = getAllLuckyTickets(tickets)
                end = time.time()

                actual_time = end - start

                with open(output_file, "r") as f:
                    expected_value = float(f.readline().strip())
                    self.assertEqual(len(lucky_tickets), expected_value)

                actual_time = end - start
                print(f"Tickets length: {tickets_length}")
                print(f"Expected value: {expected_value}")
                print(f"Actual value: {len(lucky_tickets)}")
                print(f"Actual time: {actual_time}")
                print()


if __name__ == '__main__':
    unittest.main()
