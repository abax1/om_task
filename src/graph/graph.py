from src.utils.logger import logger
from collections import defaultdict


class Graph:
    """
    This class represents a graph containing the nodes and the cost (or weight) to move from one node to an
    adjacent node.
    """
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight

