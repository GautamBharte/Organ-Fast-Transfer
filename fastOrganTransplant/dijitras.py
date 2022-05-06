# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
import sys
import fastOrganTransplant.algorithm as alg
import fastOrganTransplant.organAvl as avl


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.shortestDistance = {}

    def printSolution(self, dist):
        # print("Vertex \tDistance from Source")
        for node in range(self.V):
            # print(node, "\t", dist[node])
            self.shortestDistance[node] = dist[node]
        return self.shortestDistance
            
        

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree

    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            x = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        return self.printSolution(dist)


# if __name__ == '__main__':
#     adjlist = alg.getgraphArray()
#     noOfNodes = len(adjlist)
    
#     g = Graph(noOfNodes)
#     g.graph = adjlist

#     obj = avl.data()
#     source = 3523
#     organ = 'Heart'
    
#     index = obj.getIndexByUniqueID(source)
#     sourceInfo = obj.getbyuniqueID(source)   #return array of information about source hospital
#     availibilityList = obj.checkAvl(organ)   #return array of index with available organ
#     shortestPath = g.dijkstra(index)         #gives dictionary of shortest path of all node 
    
#     print(sourceInfo)
#     print(availibilityList)
#     print(shortestPath)
    
    
#     for node in list(shortestPath):
#         # print(node)
#         if node not in availibilityList:
#             shortestPath.pop(node)
#         if node == sourceInfo[0]:
#             shortestPath.pop(node)
    
#     lists = shortestPath.keys()
    
#     print(obj.getbyuniqueID(3522))
#     print(adjlist)
#     print(shortestPath)
