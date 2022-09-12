from decimal import Decimal

def DD_to_QDS(lat, long):

    if lat > 0 or long < 0:
        raise Exception("invalid coordinates")

    # remove '-' & split at decimal point
    if lat < 0:
        pos_lat = -1 * lat
    else:
        pos_lat = lat
    split_lat = str(pos_lat).split('.')
    int_lat = int(split_lat[0])
    dec_lat = Decimal(pos_lat) % 1

    if long < 0:
        pos_long = -1 * long
    else:
        pos_long = long
    split_long = str(pos_long).split('.')
    int_long = int(split_long[0])
    dec_long = Decimal(long) % 1

    # convert degree square from int to str
    grid_lat = str(int_lat)
    grid_long = str(int_long)

    # combine degree square with quarter degree designation based on decimal value
    if dec_lat < 0.25 and dec_long < 0.25:
        qds = grid_lat + grid_long +'AA'
    elif dec_lat < 0.25 and dec_long >= 0.25 and dec_long < 0.5:
        qds = grid_lat + grid_long + 'AB'
    elif dec_lat >= 0.25 and dec_lat < 0.5 and dec_long < 0.25:
        qds = grid_lat + grid_long + 'AC'
    elif dec_lat >= 0.25 and dec_lat < 0.5 and dec_long >= 0.25 and dec_long < 0.5:
        qds = grid_lat + grid_long + 'AD'
    elif dec_lat < 0.25 and dec_long >= 0.5 and dec_long < 0.75:
        qds = grid_lat + grid_long + 'BA'
    elif dec_lat < 0.25 and dec_long >= 0.75:
        qds = grid_lat + grid_long + 'BB'
    elif dec_lat >= 0.25 and dec_lat < 0.5 and dec_long >= 0.5 and dec_long < 0.75:
        qds = grid_lat + grid_long + 'BC'
    elif dec_lat >= 0.25 and dec_lat < 0.5 and dec_long >= 0.75:
        qds = grid_lat + grid_long + 'BD'
    elif dec_lat >= 0.5 and dec_lat < 0.75 and dec_long < 0.25:
        qds = grid_lat + grid_long + 'CA'
    elif dec_lat >= 0.5 and dec_lat < 0.75 and dec_long >= 0.25 and dec_long < 0.5:
        qds = grid_lat + grid_long + 'CB'
    elif dec_lat >= 0.75 and dec_long < 0.25:
        qds = grid_lat + grid_long + 'CC'
    elif dec_lat >= 0.75 and dec_long >= 0.25 and dec_long < 0.5:
        qds = grid_lat + grid_long + 'CD'
    elif dec_lat >= 0.5 and dec_lat < 0.75 and dec_long >= 0.5 and dec_long < 0.75:
        qds = grid_lat + grid_long + 'DA'
    elif dec_lat >= 0.5 and dec_lat < 0.75 and dec_long >= 0.75:
        qds = grid_lat + grid_long + 'DB'
    elif dec_lat >= 0.75 and dec_long >= 0.5 and dec_long < 0.75:
        qds = grid_lat + grid_long + 'DC'
    elif dec_lat >= 0.75 and dec_long >= 0.75:
        qds = grid_lat + grid_long + 'DD'

    return(qds)
   