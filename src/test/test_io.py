import unittest

from src.io.io import process_input_file


class IOTestCase(unittest.TestCase):
    def test_process_input_file1(self):
        """
        Checks that the input file 1 is converted into an object that has the timestep as a key
        and the values are arrays of tuples containing the edge data.
        """
        input_file = "/home/andy/code/python/om_task/data/input_data1.txt"
        graph_data = process_input_file(input_file)
        print(graph_data)
        self.assertEqual(graph_data[0][0][0], 'A0')
        self.assertEqual(graph_data[0][0][1], 'A9')
        self.assertEqual(graph_data[0][0][2], 0.686)

        print(graph_data[0])

    def test_process_input_file2(self):
        """
        Checks that the input file 2 is converted into an object that has the timestep as a key
        and the values are arrays of tuples containing the edge data.
        """
        input_file = "/home/andy/code/python/om_task/data/input_data2.txt"
        graph_data = process_input_file(input_file)
        print(graph_data)
        self.assertEqual(graph_data[0][0][0], 'A0')
        self.assertEqual(graph_data[0][0][1], 'A9')
        self.assertEqual(graph_data[0][0][2], 0.644)


if __name__ == '__main__':
    unittest.main()
