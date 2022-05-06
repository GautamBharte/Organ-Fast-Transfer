import fastOrganTransplant.organAvl as orgAVL
import fastOrganTransplant.include as inc

def getgraphArray():
    obj = orgAVL.data()
    
    nodes, source, destination, weight = obj.graphToArray()
    graph = []
    # print(nodes)
    # print(source)
    # print(destination)
    # print(weight)
    for rowNode in range(len(nodes)):
        colRow = []
        for colNode in range(len(nodes)):
            colRow.append(0)
        graph.append(colRow)
    # print(graph)
    if len(source) == len(destination):
        for addWeight in range(len(source)):
            src = source[addWeight]
            dest = destination[addWeight]
            graph[src][dest] = weight[addWeight]
        return graph
    # print(graph)


    
    