from dd_qds_converter import DD_to_QDS

lat = -31.12750
long = 19.19194

try:
    qds_hem = DD_to_QDS(lat, long)
    print(qds_hem)
except Exception as e:
    print(e)