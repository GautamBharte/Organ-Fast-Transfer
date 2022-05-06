from turtle import pos
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from numpy import minimum, short
import fastOrganTransplant.algorithm as alg
import fastOrganTransplant.organAvl as avl
import fastOrganTransplant.dijitras as org
import fastOrganTransplant.creategraph as graph
import fastOrganTransplant.googleMap as googlemap
import fastOrganTransplant.creategraph as graphvisuals
import sys

# Create your views here.
def index(request):
    obj = avl.data()
    hospitalList = obj.gethospitalNameList()
    uniqueIDlist = obj.getuniqueIDList()
    srcdest = 'nashik'
    googlemaplink = googlemap.getlink(srcdest)
    organlist = obj.getorganlist()
    DATASET = {
        'hospitalList' : hospitalList,
        'uniqueIDlist' : uniqueIDlist,
        'googlemaplink' : googlemaplink,
        'organlist' : organlist,
        'status' : False,
    }
    return render(request, 'index.html', context=DATASET)

def getInfo(request):
    sourceId = int(request.GET['HospitalID'])
    organreq = str(request.GET['organ'])
    
    #get source information
    obj = avl.data()
    sourceDATA = obj.getbyuniqueID(sourceId)
    srcHospitalName = sourceDATA[2]
    srcHospitalAddress = sourceDATA[3]
    
    graphvisuals.createGraph()
    # get hospital list and organ list
    hospitalList = obj.gethospitalNameList()
    uniqueIDlist = obj.getuniqueIDList()
    organlist = obj.getorganlist()
    print(organlist)
    # print(uniqueIDlist)
    organs = obj.getorganlist()
    
    # apply algorithm
    index = obj.getIndexByUniqueID(sourceId)
    availibilityList = obj.checkAvl(organreq)
    # print(availibilityList)
    adjlist = alg.getgraphArray()
    noOfNodes = len(adjlist)
    # print(adjlist)
    # print(noOfNodes)
    g = org.Graph(noOfNodes)
    
    g.graph = adjlist

    source = sourceId
    organ = organreq

    shortestPath = g.dijkstra(index)
    print(shortestPath)
    print(availibilityList)
    for node in shortestPath.copy():
        if node not in availibilityList:
            shortestPath.pop(node)
        elif node == sourceDATA[0]:
            shortestPath.pop(node)
    
    # print(shortestPath)
    #get destination information
    keys = shortestPath.keys()
    values = shortestPath.values()
    print(shortestPath)
    avllist = [] 
    distance = []
    for i in keys:
        avllist.append(i)
    for j in values:
        distance.append(j)
    print(avllist)
    print(distance)
        
    closestHospitaldistance = min(shortestPath.values())
    
    key_list = list(shortestPath.keys())
    val_list = list(shortestPath.values())
    
    print(closestHospitaldistance)
    position = key_list[val_list.index(closestHospitaldistance)]
    print(position)
    
    # algorithm to remove minimum is remaining
    
    distinationId = obj.getbyIndex(position)
    distinationDATA = obj.getbyuniqueID(distinationId)
    destHospitalName = distinationDATA[2]
    destHospitalAddress = distinationDATA[3]
    
    
    srcdest = str(str(source) + "_" + str(obj.getbyIndex(position)))
    googlemaplink = googlemap.getlink(srcdest)
    
    DATASET = {
        'organreq' : organreq,
        'sourceId' : sourceId,
        'srcHospitalName' : srcHospitalName,
        'srcHospitalAddress' : srcHospitalAddress,
        'distinationId' : distinationId,
        'destHospitalName' : destHospitalName,
        'destHospitalAddress' : destHospitalAddress,
        'googlemaplink' : googlemaplink,
        'closestdistance' : closestHospitaldistance,
        'hospitalList' : hospitalList,
        'uniqueIDlist' : uniqueIDlist,
        'organlist' : organlist,
        'status' : True,
    }
    return render(request, 'index.html', context=DATASET)