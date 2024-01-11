from os import path
import pandas as pd
from dd_to_qds_converter import dd_to_qds

#SETTINGS

filepath = r'C:\NSCFTraining\PythonScripts' #empty string if local directory
filename = "Bryophyte_Endemics.csv"
latitudeField = 'Lat'
longitudeField = 'Long'

#SCRIPT
file = path.join(filepath,filename)
df = pd.read_csv(file)
df["QDS"] = None

for index, row in df.iterrows(): 
    #barcode = df_missingQDS.loc[index][0]
    lat = row.loc[latitudeField]
    long = row.loc[longitudeField]
    if lat and long:
        try:
            qds = dd_to_qds(lat, long)
            df.loc[index, "QDS"] = qds
        except:
            i = 0 #do nothing

newfilename = filename.replace('.csv', '_QDS.csv')
df.to_csv(path.join(filepath, newfilename), index = False)