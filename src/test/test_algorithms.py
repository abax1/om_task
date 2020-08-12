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

    def test_dijsktra2(self):
        """
        This test case checks that the algorithm will find the shortest path.
        """
        input_file = "/home/andy/code/python/om_task/data/test_data4.txt"
        graph_data = process_input_file(input_file)

        graphs = {}

        for timestep in graph_data:
            # print("Timestep=", timestep)
            # Create a graph for each timestep
            graphs[timestep] = Graph()
            for edge in graph_data.get(timestep):
                graphs[timestep].add_edge(*edge)

        path = dijsktra(graphs[1], 'A0', 'B2')

        print(path)

        self.assertEqual(['A0', 'B0', 'B1', 'B2'], path)

    def test_dijsktra_2(self):
        """
        This test case checks that the algorithm will find the shortest path.
        """
        input_file = "/home/andy/code/python/om_task/data/test_data3.txt"
        graph_data = process_input_file(input_file)

        graphs = {}

        for timestep in graph_data:
            # print("Timestep=", timestep)
            # Create a graph for each timestep
            graphs[timestep] = Graph()
            for edge in graph_data.get(timestep):
                graphs[timestep].add_edge(*edge)

        path = dijsktra(graphs[0], 'A0', 'A1')

        print(path)

        self.assertEqual(['A0', 'A1'], path)

    def test_tdsp_dijsktra_with_timesteps(self):
        """
        This test case will now test the time dependency aspect where according to the timestep
        a different weight will apply to an edge.
        """
        input_file = "/home/andy/code/python/om_task/data/test_data3.txt"
        graph_data = process_input_file(input_file)

        graphs = {}

        today = datetime.today()
        t = time(0, 0)  # input time value
        start_time = datetime(today.year, today.month, today.day, t.hour, t.minute)

        for timestep in graph_data:
            # print("Timestep=", timestep)
            # Create a graph for each timestep
            graphs[timestep] = Graph()
            for edge in graph_data.get(timestep):
                graphs[timestep].add_edge(*edge)

        for graph in graphs:
            print(graphs[graph].edges)
            print(graphs[graph].weights)

        print("Start Test 1")
        path = tdsp_dijsktra(graphs, start_time, 'A0', 'A1')
        print(path)
        self.assertEqual(['A0', 'B0', 'B1', 'A1'], path)

        print("Start Test 2")
        t = time(0, 0)  # input time value
        start_time = datetime(today.year, today.month, today.day, t.hour, t.minute)
        path = tdsp_dijsktra(graphs, start_time, 'B0', 'A1')
        print(path)
        self.assertEqual(['B0', 'B1', 'A1'], path)

        print("Start Test 3")
        t = time(1, 1)  # input time value
        start_time = datetime(today.year, today.month, today.day, t.hour, t.minute)
        path = tdsp_dijsktra(graphs, start_time, 'B0', 'A1')
        print(path)
        self.assertEqual(['B0', 'A1'], path)

    def test_tdsp_dijsktra_with_timesteps_real_data(self):
        """
        This test case will now test the time dependency aspect where according to the timestep
        a different weight will apply to an edge.
        """
        input_file = "/home/andy/code/python/om_task/data/input_data1.txt"
        graph_data = process_input_file(input_file)

        graphs = {}

        today = datetime.today()
        t = time(0, 0)  # input time value
        start_time = datetime(today.year, today.month, today.day, t.hour, t.minute)

        for timestep in graph_data:
            # print("Timestep=", timestep)
            # Create a graph for each timestep
            graphs[timestep] = Graph()
            for edge in graph_data.get(timestep):
                graphs[timestep].add_edge(*edge)

        for graph in graphs:
            print(graphs[graph].edges)
            print(graphs[graph].weights)

        print("Start Test 1")
        path = tdsp_dijsktra(graphs, start_time, 'B1', 'F4')
        print(path)
        self.assertEqual(['B1', 'C2', 'D3', 'E4', 'F4'], path)

    def test_tdsp_dijsktra_with_timesteps_2(self):
        """
        This test case will now test the time dependency aspect where according to the timestep
        a different weight will apply to an edge.
        """
        input_file = "/home/andy/code/python/om_task/data/test_data3.txt"
        graph_data = process_input_file(input_file)

        graphs = {}

        today = datetime.today()
        t = time(0, 0)  # input time value
        start_time = datetime(today.year, today.month, today.day, t.hour, t.minute)

        for timestep in graph_data:
            # print("Timestep=", timestep)
            # Create a graph for each timestep
            graphs[timestep] = Graph()
            for edge in graph_data.get(timestep):
                graphs[timestep].add_edge(*edge)

        for graph in graphs:
            print(graphs[graph].edges)
            print(graphs[graph].weights)

        path = tdsp_dijsktra(graphs, start_time, 'A0', 'B1')

        print(path)

        self.assertEqual(['A0', 'B0', 'B1'], path)

    def test_tdsp_dijsktra_with_timesteps_3(self):
        """
        This test case will now test the time dependency aspect where according to the timestep
        a different weight will apply to an edge.
        """
        input_file = "/home/andy/code/python/om_task/data/test_data3.txt"
        graph_data = process_input_file(input_file)

        graphs = {}

        today = datetime.today()
        t = time(0, 0)  # input time value
        start_time = datetime(today.year, today.month, today.day, t.hour, t.minute)

        for timestep in graph_data:
            # print("Timestep=", timestep)
            # Create a graph for each timestep
            graphs[timestep] = Graph()
            for edge in graph_data.get(timestep):
                graphs[timestep].add_edge(*edge)

        for graph in graphs:
            print(graphs[graph].edges)
            print(graphs[graph].weights)

        path = tdsp_dijsktra(graphs, start_time, 'A0', 'A1')

        print(path)

        self.assertEqual(['A0', 'B0', 'A1'], path)

    def test_tdsp_dijsktra_with_timesteps_4(self):
        """
        This test case will now test the time dependency aspect where according to the timestep
        a different weight will apply to an edge.
        """
        input_file = "/home/andy/code/python/om_task/data/test_data3.txt"
        graph_data = process_input_file(input_file)

        graphs = {}

        today = datetime.today()
        t = time(0, 0)  # input time value
        start_time = datetime(today.year, today.month, today.day, t.hour, t.minute)

        for timestep in graph_data:
            # print("Timestep=", timestep)
            # Create a graph for each timestep
            graphs[timestep] = Graph()
            for edge in graph_data.get(timestep):
                graphs[timestep].add_edge(*edge)

        for graph in graphs:
            print(graphs[graph].edges)
            print(graphs[graph].weights)

        path = tdsp_dijsktra(graphs, start_time, 'A0', 'A1')

        print(path)

        self.assertEqual(['A0', 'A1'], path)

    def test_tdsp_dijsktra_with_timesteps_5(self):
        """
        This test case will now test the time dependency aspect where according to the timestep
        a different weight will apply to an edge.
        """
        input_file = "/home/andy/code/python/om_task/data/test_data4.txt"
        graph_data = process_input_file(input_file)

        graphs = {}

        today = datetime.today()
        t = time(0, 0)  # input time value
        start_time = datetime(today.year, today.month, today.day, t.hour, t.minute)

        for timestep in graph_data:
            # print("Timestep=", timestep)
            # Create a graph for each timestep
            graphs[timestep] = Graph()
            for edge in graph_data.get(timestep):
                graphs[timestep].add_edge(*edge)

        for graph in graphs:
            print(graphs[graph].edges)
            print(graphs[graph].weights)

        print("Start Test 1")
        path = tdsp_dijsktra(graphs, start_time, 'A0', 'B2')
        print("Path = ", path)
        self.assertEqual(['A0', 'B0', 'B1', 'B2'], path)


if __name__ == '__main__':
    unittest.main()
