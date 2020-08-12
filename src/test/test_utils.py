import unittest
from datetime import time, datetime, timedelta
from src.utils.distance import calculate_distance
from src.utils.retro_data_structure import GeneralFullyRetroactive
from src.utils.timestep import get_timestep, convert_float_to_time


class UtilsTestCase(unittest.TestCase):
    """
    This set of tests checks the distance calculator.

    Note: this feature is not a requirement for the assessment.
    """

    def test_calculate_distance(self):
        # make sure that a lower case letter works.
        distance = calculate_distance(('A', 2), ('b', 5))
        self.assertEqual(31.622776601683793, distance)

        distance = calculate_distance(('D', 7), ('E', 3))
        self.assertEqual(41.23105625617661, distance)

        # Check that the order of the variables does not matter.
        distance = calculate_distance(('E', 3), ('D', 7))
        self.assertEqual(41.23105625617661, distance)

        # Check real data sample from input_data2.txt
        distance = calculate_distance(('A', 0), ('A', 9))
        print(distance)
        self.assertEqual(90.0, distance)

    def test_get_timestep(self):
        # Check that we get an assert if input is None...
        self.assertRaises(ValueError, get_timestep, None)

        my_time = time(1, 30)
        ts = get_timestep(t=my_time)
        self.assertEqual(1, ts)

        my_time = time(5, 0)
        ts = get_timestep(t=my_time)
        self.assertEqual(4, ts)

        my_time = time(2, 0)
        ts = get_timestep(t=my_time)
        self.assertEqual(1, ts)

        my_time = time(2, 1)
        ts = get_timestep(t=my_time)
        self.assertEqual(2, ts)

        my_time = time(11, 0)
        ts = get_timestep(t=my_time)
        self.assertEqual(9, ts)

        my_time = time(23, 59)
        ts = get_timestep(t=my_time)
        self.assertEqual(9, ts)

    def test_timeline(self):
        today = datetime.today()
        t = time(1, 0)  # input time value

        start_time = datetime(today.year, today.month, today.day, t.hour, t.minute)
        current_time = start_time + timedelta(minutes=10)

        print("start_time= ", start_time)
        print("current_time= ", current_time)
        self.assertEqual(start_time + timedelta(minutes=10), current_time)

        t = time(1, 00)
        start_time = datetime(today.year, today.month, today.day, t.hour, t.minute)
        print("start_time= ", start_time)
        ts = get_timestep(time(start_time.hour, start_time.minute))
        print("ts = ", ts)
        ct = convert_float_to_time(1.5)
        print("ct = ", ct)
        current_time = start_time + timedelta(hours=ct.hour, minutes=ct.minute)
        print("current_time = ",current_time)
        ts = get_timestep(time(current_time.hour, current_time.minute))
        print("ts = ", ts)

    def test_convert_float_to_time(self):
        t = convert_float_to_time(1.5)
        print("t = ", t)
        self.assertEqual(time(1, 30), t)

        t = convert_float_to_time(1.8)
        print("t = ", t)
        self.assertEqual(time(1, 48), t)

        t = convert_float_to_time(0.5)
        print("t = ", t)
        self.assertEqual(time(0, 30), t)


if __name__ == '__main__':
    unittest.main()
