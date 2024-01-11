from os import path
import pandas as pd
from dd_to_qds_converter import dd_to_qds

#SETTINGS

filepath = r'filepath goes here' #empty string if local directory
filename = r'file name with .csv on the end goes here'
latitudeField = 'name of your latitude field'
longitudeField = 'name of your longitude field'

#SCRIPT
file = path.join(filepath,filename)
df = pd.read_csv(file)
df["QDS"] = None

for index, row in df.iterrows(): 
    #barcode = df_missingQDS.loc[index][0]
    lat = row.loc[latitudeField]
    long = row.loc[longitudeField]
    if lat and long:

        #check they are valid numbers
        try:
            lat = float(lat)
            long = float(long)
        except:
            print(f'could not convert {lat}, {long} in row {index}: invalid format')
            continue

        # do the conversion
        try:
            qds = dd_to_qds(lat, long)
            df.loc[index, "QDS"] = qds
        except Exception as ex:
            print(f'could not convert {lat}, {long} in row {index}: {str(ex)}')
            continue

    elif lat or long:
        print(f'missing coordinate in row {index}')

newfilename = filename.replace('.csv', '_QDS.csv')
df.to_csv(path.join(filepath, newfilename), index = False)