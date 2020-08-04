import unittest

from src.graph.graph import Graph


class GraphTestCase(unittest.TestCase):
    def test_graph_init(self):
        pass

    def test_graph_init_no_input_file(self):
        self.assertRaises(ValueError, Graph)


if __name__ == '__main__':
    unittest.main()
