import unittest

from src.graph.graph import Graph
from src.io.io import process_input_file


class GraphTestCase(unittest.TestCase):
    def test_graph_init(self):
        graph = Graph()
        self.assertIsNotNone(graph, "Graph cannot be None.")

    def test_graph_init_no_input_file(self):
        # self.assertRaises(ValueError, Graph)
        # TODO
        pass

    def test_graph_add_edges(self):
        input_file = "/home/andy/code/python/om_task/data/input_data1.txt"
        graph_data = process_input_file(input_file)

        graphs = {}

        for timestep in graph_data:
            # print("Timestep=", timestep)
            # Create a graph for each timestep
            graphs[timestep] = Graph()
            for edge in graph_data.get(timestep):
                graphs[timestep].add_edge(*edge)

        # print("Check weights...")
        # print(graph_data.keys())
        # print(graphs.keys())
        self.assertEqual(graphs.get(0).weights[('A0', 'A9')], 0.686)



if __name__ == '__main__':
    unittest.main()
