from decimal import Decimal

qds1 = "3018AB (-30.23667, 18.49639)"
qds2 = "3321AD (-33.34555, 21.47778)"
qds3 = "3320BB (-33.14917, 20.87083)"
qds4 = "3119AA (-31.12750, 19.19194)"

lat = -31.12750
long = 19.19194

def convertQDS(lat, long):

    if lat < 0:
        pos_lat = -1 * lat
    else:
        pos_lat = lat
    split_lat = str(pos_lat).split('.')
    int_lat = int(split_lat[0])
    dec_lat = Decimal(pos_lat) % 1
    print(int_lat)
    print(dec_lat)

    if long < 0:
        pos_long = -1 * long
    else:
        pos_long = long
    split_long = str(pos_long).split('.')
    int_long = int(split_long[0])
    dec_long = Decimal(long) % 1
    print(int_long)
    print(dec_long)

    grid_lat = str(int_lat)
    print(grid_lat)
    grid_long = str(int_long)
    print(grid_long)

    if dec_lat <= 0.24999 and dec_long <= 0.24999:
        print(grid_lat + grid_long +'AA')
    elif dec_lat <= 0.249 and dec_long >= 0.25 and dec_long <= .49:
        print(grid_lat + grid_long + 'AB')
    elif dec_lat >= 0.25 and dec_lat <= 0.49 and dec_long <= 0.249:
        print(grid_lat + grid_long + 'AC')
    elif dec_lat >= 0.25 and dec_lat <= 0.49 and dec_long >= 0.25 and dec_long <= 0.49:
        print(grid_lat + grid_long + 'AD')
    elif dec_lat <= 0.249 and dec_long >= 0.5 and dec_long <= 0.749:
        print(grid_lat + grid_long + 'BA')
    elif dec_lat <= 0.249 and dec_long >= 0.75:
        print(grid_lat + grid_long + 'BB')
    elif dec_lat >= 0.25 and dec_lat <= 0.49 and dec_long >= 0.5 and dec_long <= 0.749:
        print(grid_lat + grid_long + 'BC')
    elif dec_lat >= 0.25 and dec_lat <= 0.49 and dec_long >= 0.75:
        print(grid_lat + grid_long + 'BD')
    elif dec_lat >= 0.5 and dec_lat <= 0.749 and dec_long <= 0.249:
        print(grid_lat + grid_long + 'CA')
    elif dec_lat >= 0.5 and dec_lat <= 0.749 and dec_long >= 0.25 and dec_long <= 0.49:
        print(grid_lat + grid_long + 'CB')
    elif dec_lat >= 0.75 and dec_long <= 0.249:
        print(grid_lat + grid_long + 'CC')
    elif dec_lat >= 0.75 and dec_long >= 0.25 and dec_long <= 0.49:
        print(grid_lat + grid_long + 'CD')
    elif dec_lat >= 0.5 and dec_lat <= 0.749 and dec_long >= 0.5 and dec_long <= 0.749:
        print(grid_lat + grid_long + 'DA')
    elif dec_lat >= 0.5 and dec_lat <= 0.749 and dec_long >= 0.75:
        print(grid_lat + grid_long + 'DB')
    elif dec_lat >= 0.75 and dec_lat >= 0.5 and dec_long <= 0.749:
        print(grid_lat + grid_long + 'DC')
    elif dec_lat >= 0.75 and dec_lat >= 0.75:
        print(grid_lat + grid_long + 'DD')

convertQDS (-31.12750, 19.19194)
