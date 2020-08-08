from src.utils.timestep import get_timestep, convert_float_to_time
from datetime import time, datetime, timedelta

def dijsktra(graph, initial, end):
    """
    Dijsktra's shortest path algorithm.

    :param graph: The graph containing the nodes and edges
    :param initial: The start node
    :param end: The destination node
    :return: An ordered list of nodes that gives the shortest calculated path
    """
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]
        print("shortest_paths = ", shortest_paths)

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}

        if not next_destinations:
            return "Route not possible"

        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node

    # Reverse the path
    path = path[::-1]
    return path


def tdsp_dijsktra(graphs, start_time, initial, end):
    """
    A time-dependent version of Dijsktra's shortest path algorithm.

    :param graphs: The graph containing the nodes and edges
    :param start_time: The planned start time
    :param initial: The start node
    :param end: The destination node
    :return: An ordered list of nodes that gives the shortest calculated path
    """
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    ts = get_timestep(time(start_time.hour, start_time.minute))
    current_time = start_time

    while current_node != end:
        visited.add(current_node)
        destinations = graphs[ts].edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]
        print("weight_to_current_node = ", weight_to_current_node)
        print("shortest_paths = ", shortest_paths)
        print("destinations = ", destinations)

        for next_node in destinations:
            weight = graphs[ts].weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

            # update the time.
            ct = convert_float_to_time(shortest_paths[next_node][1])
            print("ct = ", ct)
            current_time += timedelta(hours=ct.hour, minutes=ct.minute)
            ts = get_timestep(time(current_time.hour, current_time.minute))
            print("ts = ", ts)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        print("next_destinations = ", next_destinations)

        if not next_destinations:
            return "Route not possible"

        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node

    # Reverse the path
    path = path[::-1]
    return path
