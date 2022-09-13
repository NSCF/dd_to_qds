from dd_to_qds_converter import DD_to_QDS

lat = -34.26667		
long = 18.46667

try:
    qds = dd_to_qds(lat, long)
    print(qds)
except Exception as e:
    print(e)