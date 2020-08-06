import unittest

from src.algorithms.tdsp_dijsktra import tdsp_dijsktra
from src.graph.graph import Graph
from src.io.io import process_input_file


class AlgoTestCase(unittest.TestCase):
    def test_tdsp_dijsktra(self):
        input_file = "/home/andy/code/python/om_task/data/test_data.txt"
        graph_data = process_input_file(input_file)

        graphs = {}

        for timestep in graph_data:
            # print("Timestep=", timestep)
            # Create a graph for each timestep
            graphs[timestep] = Graph()
            for edge in graph_data.get(timestep):
                graphs[timestep].add_edge(*edge)

        path = tdsp_dijsktra(graphs[0], 'A0', 'B2')

        print(path)

        self.assertEqual(path, ['A0', 'A1', 'A2', 'B2'])


if __name__ == '__main__':
    unittest.main()
