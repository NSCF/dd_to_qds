from decimal import Decimal

def dd_qds(ddLat, ddLng):
    try:
        float(ddLat) and float(ddLng)
        
        Lat = 'N'
        Lng = 'E'

        # need to fix if there are ','s instead of '.'
        if ',' in ddLat:
            ddLat = ddLat.replace(',','.')
        if ',' in ddLng:
            ddLng = ddLng.replace(',', '.')

        #get rid of "-"
        ddLat = float(ddLat)
        if ddLat < 0:
            Lat = 'S'
            ddLat = -1 * ddLat
        if ddLat > 90:
            raise Exception("Invalid Latitude")
            
        ddLng = float(ddLng)
        if ddLng < 0:
            Lng = 'W'
            ddLng = -1 * ddLng
        if ddLng > 180:
            raise Exception("Invalid Longitude")

        ddLat = round(ddLat, 5)
        print(ddLat)
        ddLng = round(ddLng, 5)
        print(ddLng)

        ddLat = str(ddLat)
        ddLng = str(ddLng)

    # split ddLat and ddLng on '.'
        lat = ddLat.split(".")
        print(lat)
        lng = ddLng.split(".")
        print(lng)

    #concatenate degreeLat + degreeLng
        qds =(lat[0]) + (lng[0])
        print(qds)

    #get letters from decimals
        ddLatdec = Decimal(ddLat) % 1
        print(ddLatdec)
        ddLngdec = Decimal(ddLng) % 1
        print(ddLngdec)

        if 0.00000 <= ddLatdec < 0.50000 and 0.00000 <= ddLngdec < 0.50000:
            qds1 = 'A'
        elif 0.00000 <= ddLatdec < 0.50000 and 0.50000 <= ddLngdec < 1.0000:
            qds1 = 'B'
        elif 0.50000 <= ddLatdec < 1.00000 and 0.00000 < ddLngdec < 0.50000:
            qds1 = 'C'
        elif 0.50000 <= ddLatdec < 1.00000 and 0.50000 <= ddLngdec < 1.00000:
            qds1 = 'D' 

        if 0.00000 <= ddLatdec < 0.25000 and (0.00000 <= ddLngdec < 0.25000 or 0.50000 <= ddLngdec < 0.75000):
            qds2 = 'A'
        elif 0.50000 <= ddLatdec < 0.75000 and (0.00000 <= ddLngdec < 0.25000 or 0.50000 <= ddLngdec < 0.75000):
            qds2 = 'A'  
        elif 0.00000 <= ddLatdec < 0.25000 and (0.25000 <= ddLngdec < 0.50000 or 0.75000 <= ddLngdec < 1.00000):
            qds2 = 'B'  
        elif 0.50000 <= ddLatdec < 0.75000 and (0.25000 <= ddLngdec < 0.50000 or 0.75000 <= ddLngdec < 1.00009):
            qds2 = 'B'
        elif 0.25000 <= ddLatdec < 0.50000 and (0.00000 <= ddLngdec < 0.25000 or 0.50000 <= ddLngdec < 0.75000):
            qds2 = 'C'
        elif 0.75000 <= ddLatdec < 1.00000 and (0.00000 <= ddLngdec < 0.25000 or 0.50000 <= ddLngdec < 0.75000):
            qds2 = 'C'
        elif 0.25000 <= ddLatdec < 0.50000 and (0.25000 <= ddLngdec < 0.50000 or 0.75000 <= ddLngdec < 1.00000):
            qds2 = 'D'
        elif 0.75000 <= ddLatdec < 1.00000 and (0.25000 <= ddLngdec < 0.50000 or 0.75000 <= ddLngdec < 1.00000):
            qds2 = 'D'
        # else:
        #     raise Exception("Invalid coordinates")

        qds = qds + qds1 + qds2 + ' Hemisphere: '+ Lat + Lng
        return(qds)

    except Exception as e:
        print("Invalid coordinates")  