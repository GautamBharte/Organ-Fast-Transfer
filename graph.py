# G = (V, E)
from collections import namedtuple

from pyvis.network import Network

Graph = namedtuple("Graph", ["nodes", "edges", "is_directed"])


def adjacency_dict(graph):
    """
    Returns the adjacency list representation
    of the graph.
    """
    adj = {node: [] for node in graph.nodes}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1].append(node2)
        if not graph.is_directed:
            adj[node2].append(node1)
    return adj


def adjacency_matrix(graph):
    """
    Returns the adjacency matrix of the graph.

    Assumes that graph.nodes is equivalent to range(len(graph.nodes)).
    """
    adj = [[0 for node in graph.nodes] for node in graph.nodes]
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1][node2] += 1
        if not graph.is_directed:
            adj[node2][node1] += 1
    return adj


def show(graph, output_filename):
    """
    Saves an HTML file locally containig a 
    visualization
    """
    g = Network(directed=graph.is_directed)
    g.add_nodes(graph.nodes)
    g.add_edges(graph.edges)
    g.show(output_filename)
    return g
