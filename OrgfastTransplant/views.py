from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import OrgfastTransplant.algorithm as alg
import OrgfastTransplant.organAvl as avl
import OrgfastTransplant.dijitras as org
import OrgfastTransplant.creategraph as graph
import sys


# Create your views here.
def index(request):
    obj = avl.data()
    
    hospitalList = obj.gethospitalNameList()
    organs = obj.getorganlist()
    graph.createGraph()
    DATASET = {
        'hospitalList' : hospitalList,
        'organs' : organs,
    }
    return render(request, 'index.html', context=DATASET)

def viewcitymap(request):
    # graphview = graph.createGraph()
    return render(request, 'graph.html')

def getInfo(request):
    uniqueID = str(request.GET['uniqueID'])
    organreq = str(request.GET['organ'])
    obj = avl.data()
    
    hospitalList = obj.gethospitalNameList()
    # print(hospitalList)
    adjlist = alg.getgraphArray()
    noOfNodes = len(adjlist)
    
    g = org.Graph(noOfNodes)
    g.graph = adjlist

    source = 3521
    organ = organreq
    
    index = obj.getIndexByUniqueID(source)
    sourceInfo = obj.getbyuniqueID(source)   #return array of information about source hospital
    availibilityList = obj.checkAvl(organ)   #return array of index with available organ
    # print(index)
    # print(availibilityList)
    
    
    shortestPath = g.dijkstra(index)         #gives dictionary of shortest path of all node 
    # print(shortestPath)
    
    for node in list(shortestPath):
        # print(node)
        if node not in availibilityList:
            shortestPath.pop(node)
        if node == sourceInfo[0]:
            shortestPath.pop(node)
    
    lists = shortestPath.keys()
    
    print(obj.getbyuniqueID(3522))
    sourcehospitalID  = sourceInfo[1]
    sourceHospitalName = sourceInfo[2]
    sourceHospitalAddress = sourceInfo[3]
    
    DATASET = {
        'uniqueID' : uniqueID,
        'organ' : organreq,
        'status' : True,
        'source_hospitalID' : sourceInfo,
        'availibilityList' : availibilityList,
        'shortestPath' : shortestPath,
        'hospitalList' : hospitalList,
        'sourcehospitalID' : sourcehospitalID,
        'sourceHospitalName' : sourceHospitalName,
        'sourceHospitalAddress' : sourceHospitalAddress
    }
    return render(request, 'index.html', context=DATASET)