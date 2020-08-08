import unittest
from datetime import time, datetime, timedelta
from src.algorithms.tdsp_dijsktra import tdsp_dijsktra, dijsktra
from src.graph.graph import Graph
from src.io.io import process_input_file


class AlgoTestCase(unittest.TestCase):
    def test_dijsktra(self):
        """
        This test case checks that the algorithm will find the shortest path.
        """
        input_file = "/home/andy/code/python/om_task/data/test_data.txt"
        graph_data = process_input_file(input_file)

        graphs = {}

        for timestep in graph_data:
            # print("Timestep=", timestep)
            # Create a graph for each timestep
            graphs[timestep] = Graph()
            for edge in graph_data.get(timestep):
                graphs[timestep].add_edge(*edge)

        path = dijsktra(graphs[0], 'A0', 'B2')

        print(path)

        self.assertEqual(['A0', 'A1', 'A2', 'B2'], path)

    def test_tdsp_dijsktra_with_timesteps(self):
        """
        This test case will now test the time dependency aspect where according to the timestep
        a different weight will apply to an edge.
        """
        input_file = "/home/andy/code/python/om_task/data/test_data.txt"
        graph_data = process_input_file(input_file)

        graphs = {}

        today = datetime.today()
        t = time(1, 0)  # input time value
        start_time = datetime(today.year, today.month, today.day, t.hour, t.minute)



        for timestep in graph_data:
            # print("Timestep=", timestep)
            # Create a graph for each timestep
            graphs[timestep] = Graph()
            for edge in graph_data.get(timestep):
                graphs[timestep].add_edge(*edge)

        path = tdsp_dijsktra(graphs, start_time, 'A0', 'B2')

        print(path)

        self.assertEqual(['A0', 'A1', 'B2'], path)


if __name__ == '__main__':
    unittest.main()
