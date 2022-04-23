import pandas as pd
import include as inc
from os import *

class data:
    # hospital_data_path = Path('Database/hospital_data.csv') 
    # graph_info_path = Path('Database/graph_info.csv')
    def __init__(self, hospitalpath, graphpath):
        self.hospital_data_path = hospitalpath
        self.graph_info_path = graphpath
        self.hospital_data = pd.read_csv(hospital_data_path, header = 0)
        self.graph_info = pd.read_csv(graph_info_path, header = 0)
    def getHospitaldata(self):
        return self.hospital_data
    def getGraphdata(self):
        return self.graph_info
    def checkAvl(self, organ):
        avlList = self.hospital_data.uniqueID[self.hospital_data[organ]].tolist()
        return avlList
    def getbyuniqueID(self, uniqueID):
        return self.hospital_data.loc[self.hospital_data['uniqueID'] == uniqueID]
    
if __name__ == '__main__':
    hospital_data_path = inc.hospital_data_path
    graph_info_path = inc.graph_info_path
    
    obj = data(hospital_data_path, graph_info_path)
    print(obj.getHospitaldata())
    print(obj.checkAvl('Heart'))
    print(obj.getbyuniqueID(3522))