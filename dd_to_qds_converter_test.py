import csv
import pandas as pd
#from dd_to_qds_bulk import dd_to_qds_bulk
from dd_to_qds_converter import dd_to_qds


df_missingQDS = pd.read_csv("missingQDS_test.csv")
#print(df_missingQDS)
#df_missingQDS["QDS"] = None
df_missingQDS["QDS"] = None
# df_missingQDS["QDS"] == dd_to_qds(df_missingQDS['decimalLatitude'], df_missingQDS["decimalLongitude"])
# df_missingQDS.to_csv('C:\\Users\\01470358\\Documents\\DevProjects\\dd_to_qds\\missingQDS_newQDS.csv', index = False)

for index, row in df_missingQDS.iterrows(): 
    #barcode = df_missingQDS.loc[index][0]
    lat = row.loc["decimalLatitude"]
    long = row.loc["decimalLongitude"]
    qds = dd_to_qds(lat, long)
    df_missingQDS["QDS"] = qds
df_missingQDS.to_csv('missingQDS_newQDS.csv', index = False)

# df_missingQDS = pd.read_csv("missingQDS_test.csv")
# #print(df_missingQDS)
# df_missingQDS["QDS"] = None

# for index, row in df_missingQDS.iterrows(): 
#     #barcode = df_missingQDS.loc[index][0]
#     lat = row.loc["decimalLatitude"]
#     long = row.loc["decimalLongitude"]
#     qds = dd_to_qds(lat, long)
#     df_missingQDS.loc[index, "QDS"] = qds

# df_missingQDS.to_csv('C:\\Users\\01470358\\Documents\\DevProjects\\dd_to_qds\\missingQDS_newQDS.csv', index = False)


# header = ["barcode", "lat", "long", "qds"]

# with open('C:\\Users\\01470358\\Documents\\DevProjects\\dd_to_qds\\missingQDS_output.csv', 'w',  newline = "") as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     try:
#         for index, row in df_missingQDS.iterrows(): 
#             barcode = df_missingQDS.loc[index][0]
#             lat = df_missingQDS.loc[index][1]
#             long = df_missingQDS.loc[index][2]
#             qds = dd_to_qds_bulk(lat, long)
#             #print(barcode, lat, long, qds)
#             data = [barcode, lat, long, qds]
#             writer.writerow(data)
#     except Exception as e:
#         print(e)

# f.close()


# #df_missingQDS.to_csv