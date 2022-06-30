from dd_to_qds import dd_qds

test = '-25.25000 31.0113888'
# test = '30.558436789 18.91185'
# test = '-34.5589167 -31.01246'


ddLat = '-34.5589167'
ddLng = '-31.01246'

try:
    qds = dd_qds(ddLat, ddLng)
    print(qds)
except Exception as e:
    print(e)