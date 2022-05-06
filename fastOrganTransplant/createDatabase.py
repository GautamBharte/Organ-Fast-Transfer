import pandas as pd
from pathlib import Path
from os import *

if __name__ == '__main__':
    hospital_data = pd.DataFrame({'uniqueID' : [3521, 3522, 3523,],
                                'hospitalName' : ['Appolo Hospital', 'Siddhi Vinayak Hospital', 'Apex Hospital'],
                                'location' : ['Minabai Thakre Stadium', 'Gangapur Road', 'Indra Nagar'],
                                'coordinates' : ['0,0', '15,224', '567,345'],
                                'Liver' : [True, False, False],
                                'Kidney' : [False, False, False],
                                'Pancreas' : [True, False, True],
                                'Heart' : [True, True, False],
                                'Corneas' : [True, True, True],
                                'Bone Marrow' : [True, False, False]})

    graph_info = pd.DataFrame({'source' : [0, 1, 1, 2, 0, 2],
                            'destination' : [1, 0, 2, 1, 2, 0],
                            'weight' : [20, 20, 17, 17, 26, 26]})

    hospital_data_path = Path('hospital_data.csv') 
    graph_info_path = Path('graph_info.csv')
    hospital_data.to_csv(hospital_data_path, index=True)
    graph_info.to_csv(graph_info_path, index=True)