# G = (V, E)
from collections import namedtuple
from operator import length_hint
from platform import node

from pyvis.network import Network
import OrgfastTransplant.organAvl as orgAvl

import random


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
    visualization of the graph, and returns
    a pyvis Network instance of the graph.
    """
    g = Network(directed=graph.is_directed)
    g.add_nodes(graph.nodes)
    g.add_edges(graph.edges)
    g.show(output_filename)
    return g

def createGraph():
    obj = orgAvl.data()
    nodes = obj.getNodes()
    # print(nodes)
    sourcedest = obj.sourceDestArray()
    # print(sourcedest)


    net = Network()
    length = len(nodes)
    # print(length)
    for eachnode in nodes:
        net.add_node(eachnode, color='#f00ff1e')
    for eachedge in sourcedest:
        net.add_edge(eachedge[0], eachedge[1], weight=eachedge[2], color='#FF0000')


    # net.show("./templates/graph.html")
    
# if __name__ == '__main__':
#     createGraph()
