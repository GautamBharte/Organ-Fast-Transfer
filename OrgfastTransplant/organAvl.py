import pandas as pd
import OrgfastTransplant.include as inc
from os import *

class data:
    # hospital_data_path = Path('Database/hospital_data.csv') 
    # graph_info_path = Path('Database/graph_info.csv')
    def __init__(self):
        self.hospital_data_path = inc.hospital_data_path
        self.graph_info_path = inc.graph_info_path
        self.hospital_data = pd.read_csv(self.hospital_data_path, header = 0)
        self.graph_info = pd.read_csv(self.graph_info_path, header = 0)
    def getHospitaldata(self):
        return self.hospital_data
    def getGraphdata(self):
        return self.graph_info
    def checkAvl(self, organ):
        avlList = self.hospital_data.index[self.hospital_data[organ]].tolist()
        return avlList
    def getbyuniqueID(self, uniqueID):
        return self.hospital_data.loc[self.hospital_data['uniqueID'] == uniqueID].values.tolist()[0]
    def getIndexByUniqueID(self, uniqueID):
        data = self.getbyuniqueID(uniqueID)
        return data[0]
    def graphToArray(self):
        nodes = self.hospital_data.index[self.hospital_data.index].tolist()
        source = self.graph_info["source"].tolist()
        destination = self.graph_info["destination"].tolist()
        weight = self.graph_info["weight"].tolist()
        return nodes, source, destination, weight
    def getbyHospitalName(self, hospitalName):
        hospitaldata = self.hospital_data.loc[self.hospital_data['hospitalName'] == hospitalName].values.tolist()[0]
        return hospitaldata
    def gethospitalNameList(self):
        hospitalList = self.hospital_data['hospitalName'].tolist()
        return hospitalList
    def getorganlist(self):
        organs = list(self.hospital_data.columns)
        organs = organs[5:]
        return organs
    def getNodes(self):
        return self.hospital_data.index[self.hospital_data.index].tolist()
    def sourceDestArray(self):
        source = self.graph_info["source"].tolist()
        destination = self.graph_info["destination"].tolist()
        weight = self.graph_info["weight"].tolist()
        # print(source)
        # print(destination)
        array = []
        for getegde in range(len(source)):
            if getegde%2 == 0:
                edge = []
                edge.append(source[getegde])
                edge.append(destination[getegde])
                edge.append(weight[getegde])
                array.append(edge)
        return array
    
