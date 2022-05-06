# G = (V, E)
from collections import namedtuple
from operator import length_hint
from platform import node
from xml.dom.minicompat import NodeList
from numpy import char

from pyvis.network import Network
import fastOrganTransplant.organAvl as orgAvl

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
    hospitalname = obj.gethospitalNameList()
    # print(hospitalname)
    nodes = obj.getNodes()
    # print(nodes)
    sourcedest = obj.sourceDestArray()
    # print(sourcedest)

    # print(obj.getbyuniqueID(obj.getbyIndex(0))[2])

    srcdestarr = []
    for i in sourcedest:
        empty = []
        empty.append(obj.getbyuniqueID(obj.getbyIndex(i[0]))[2])
        empty.append(obj.getbyuniqueID(obj.getbyIndex(i[1]))[2])
        empty.append(i[2])
        srcdestarr.append(empty)
    print(srcdestarr)

    net = Network()
    length = len(nodes)
    # print(length)
    # for eachnode in nodes:
    #     net.add_node(eachnode, color='#f00ff1e')
    x=10
    y=5
    for eachname in hospitalname:
        net.add_node(eachname, color='#0AA1DD', id=eachname, x=x, y=y)
        x=x+50
        y=y+30
    for eachedge in srcdestarr:
        net.add_edge(eachedge[0], eachedge[1],
                     weight=eachedge[2], label=eachedge[2], color='#2155CD')

    neighbor_map = net.get_adj_list()

    # for node in net.nodes:
    #     # print(node)
    #     node['label']  # += ' Neighbors:'<br> + \
    #     # '<br>'.join(neighbor_map[node['id']])
    #     node['value'] = len(neighbor_map[node['id']])
    net.toggle_physics("false")
    net.show("./templates/graph.html")


if __name__ == '__main__':
    createGraph()
