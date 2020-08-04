import unittest

from src.utils.distance import calculate_distance


class DistanceCalcTestCase(unittest.TestCase):
    """This set of tests checks the distance calculator."""

    def test_calculate_distance(self):

        # make sure that a lower case letter works.
        distance = calculate_distance(('A', 2), ('b', 5))
        self.assertEqual(distance, 31.622776601683793)

        distance = calculate_distance(('D', 7), ('E', 3))
        self.assertEqual(distance, 41.23105625617661)

        # Check that the order of the variables does not matter.
        distance = calculate_distance(('E', 3), ('D', 7))
        self.assertEqual(distance, 41.23105625617661)

        # Check real data sample from input_data2.txt
        distance = calculate_distance(('A', 0), ('A', 9))
        print(distance)
        self.assertEqual(distance, 90.0)


if __name__ == '__main__':
    unittest.main()
