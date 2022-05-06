# G = (V, E)
from collections import namedtuple
from operator import length_hint
from platform import node
from turtle import window_width
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

    # Adding the hospitals
    xcoordinate = [1100, 800, 500, 100, 1100, 1300, 1400, 1200, 600, 500]
    ycoordinate = [200, 500, 400, 700, 1000, 1100, 400, 1200, 600, 900]
    for i in range(len(hospitalname)):
        net.add_node(hospitalname[i], color='#0AA1DD',
                     id=hospitalname[i], x=xcoordinate[i], y=ycoordinate[i])

    # for eachname in hospitalname:
    #     net.add_node(eachname, color='#0AA1DD', id=eachname, x=x, y=y)
    #     x=x+50
    #     y=y+30
    net.add_edge(hospitalname[0], hospitalname[1],
                 weight=5.1, label=5.1, width=3, color='#2155CD')
    net.add_edge(hospitalname[0], hospitalname[6],
                 weight=5.4, label=5.4, width=3, color='#2155CD')
    net.add_edge(hospitalname[1], hospitalname[0],
                 weight=5.1, label=5.1, width=3, color='#2155CD')
    net.add_edge(hospitalname[1], hospitalname[6],
                 weight=2.6, label=2.6, width=3, color='#2155CD')
    net.add_edge(hospitalname[1], hospitalname[4],
                 weight=3.3, label=3.3, width=3, color='#2155CD')
    net.add_edge(hospitalname[1], hospitalname[8],
                 weight=1.9, label=1.9, width=3, color='#2155CD')
    net.add_edge(hospitalname[1], hospitalname[2],
                 weight=0.8, label=0.8, width=3, color='#2155CD')
    net.add_edge(hospitalname[2], hospitalname[1],
                 weight=0.8, label=0.8, width=3, color='#2155CD')
    net.add_edge(hospitalname[2], hospitalname[8],
                 weight=2.2, label=2.2, width=3, color='#2155CD')
    net.add_edge(hospitalname[2], hospitalname[3],
                 weight=3.1, label=3.1, width=3, color='#2155CD')
    net.add_edge(hospitalname[3], hospitalname[2],
                 weight=3.1, label=3.1, width=3, color='#2155CD')
    net.add_edge(hospitalname[3], hospitalname[9],
                 weight=2.7, label=2.7, width=3, color='#2155CD')
    net.add_edge(hospitalname[4], hospitalname[7],
                 weight=3.4, label=3.4, width=3, color='#2155CD')
    net.add_edge(hospitalname[4], hospitalname[5],
                 weight=1.9, label=1.9, width=3, color='#2155CD')
    net.add_edge(hospitalname[4], hospitalname[9],
                 weight=2.9, label=2.9, width=3, color='#2155CD')
    net.add_edge(hospitalname[4], hospitalname[8],
                 weight=5.0, label=5.0, width=3, color='#2155CD')
    net.add_edge(hospitalname[4], hospitalname[1],
                 weight=3.3, label=3.3, width=3, color='#2155CD')
    net.add_edge(hospitalname[4], hospitalname[6],
                 weight=3.5, label=3.5, width=3, color='#2155CD')
    net.add_edge(hospitalname[5], hospitalname[6],
                 weight=9.2, label=9.2, width=3, color='#2155CD')
    net.add_edge(hospitalname[5], hospitalname[4],
                 weight=1.9, label=1.9, width=3, color='#2155CD')
    net.add_edge(hospitalname[5], hospitalname[7],
                 weight=1.7, label=1.7, width=3, color='#2155CD')
    net.add_edge(hospitalname[6], hospitalname[0],
                 weight=5.4, label=5.4, width=3, color='#2155CD')
    net.add_edge(hospitalname[6], hospitalname[1],
                 weight=2.6, label=2.6, width=3, color='#2155CD')
    net.add_edge(hospitalname[6], hospitalname[4],
                 weight=3.5, label=3.5, width=3, color='#2155CD')
    net.add_edge(hospitalname[6], hospitalname[5],
                 weight=9.2, label=9.2, width=3, color='#2155CD')
    net.add_edge(hospitalname[7], hospitalname[4],
                 weight=3.4, label=3.4, width=3, color='#2155CD')
    net.add_edge(hospitalname[7], hospitalname[5],
                 weight=1.7, label=1.7, width=3, color='#2155CD')
    net.add_edge(hospitalname[8], hospitalname[2],
                 weight=2.2, label=2.2, width=3, color='#2155CD')
    net.add_edge(hospitalname[8], hospitalname[1],
                 weight=1.9, label=1.9, width=3, color='#2155CD')
    net.add_edge(hospitalname[8], hospitalname[4],
                 weight=5.0, label=5.0, width=3, color='#2155CD')
    net.add_edge(hospitalname[8], hospitalname[9],
                 weight=2.3, label=2.3, width=3, color='#2155CD')
    net.add_edge(hospitalname[9], hospitalname[3],
                 weight=2.7, label=2.7, width=3, color='#2155CD')
    net.add_edge(hospitalname[9], hospitalname[8],
                 weight=2.3, label=2.3, width=3, color='#2155CD')
    net.add_edge(hospitalname[9], hospitalname[4],
                 weight=2.9, label=2.9, width=3, color='#2155CD')

    # neighbor_map = net.get_adj_list()

    # for node in net.nodes:
    #     # print(node)
    #     node['label']  # += ' Neighbors:'<br> + \
    #     # '<br>'.join(neighbor_map[node['id']])
    #     node['value'] = len(neighbor_map[node['id']])
    net.toggle_physics("false")
    net.show("./templates/graph.html")


width = 3,
if __name__ == '__main__':
    createGraph()
