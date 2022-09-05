from DD_QDS_Converter import DD_to_QDS

lat = -31.12750
long = 19.19194

try:
    qds = DD_to_QDS(lat, long)
    print(qds)
except Exception as e:
    print(e)