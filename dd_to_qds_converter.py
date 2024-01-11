from decimal import Decimal

def dd_to_qds(lat, long):

    #southern africa and madagascar only
    if lat > 0 or lat < -35 or long < 0 or long > 51:
        raise Exception("coordinates out of bounds")

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
    qds = str(int_lat) + str(int_long)

    # combine degree square with quarter degree letters based on decimal value
    if dec_lat < 0.25 and dec_long < 0.25:
        qds +='AA'
    elif dec_lat < 0.25 and dec_long >= 0.25 and dec_long < 0.5:
        qds += 'AB'
    elif dec_lat >= 0.25 and dec_lat < 0.5 and dec_long < 0.25:
        qds += 'AC'
    elif dec_lat >= 0.25 and dec_lat < 0.5 and dec_long >= 0.25 and dec_long < 0.5:
        qds += 'AD'
    elif dec_lat < 0.25 and dec_long >= 0.5 and dec_long < 0.75:
        qds += 'BA'
    elif dec_lat < 0.25 and dec_long >= 0.75:
        qds += 'BB'
    elif dec_lat >= 0.25 and dec_lat < 0.5 and dec_long >= 0.5 and dec_long < 0.75:
        qds += 'BC'
    elif dec_lat >= 0.25 and dec_lat < 0.5 and dec_long >= 0.75:
        qds += 'BD'
    elif dec_lat >= 0.5 and dec_lat < 0.75 and dec_long < 0.25:
        qds += 'CA'
    elif dec_lat >= 0.5 and dec_lat < 0.75 and dec_long >= 0.25 and dec_long < 0.5:
        qds += 'CB'
    elif dec_lat >= 0.75 and dec_long < 0.25:
        qds += 'CC'
    elif dec_lat >= 0.75 and dec_long >= 0.25 and dec_long < 0.5:
        qds += 'CD'
    elif dec_lat >= 0.5 and dec_lat < 0.75 and dec_long >= 0.5 and dec_long < 0.75:
        qds += 'DA'
    elif dec_lat >= 0.5 and dec_lat < 0.75 and dec_long >= 0.75:
        qds += 'DB'
    elif dec_lat >= 0.75 and dec_long >= 0.5 and dec_long < 0.75:
        qds += 'DC'
    elif dec_lat >= 0.75 and dec_long >= 0.75:
        qds += 'DD'

    return(qds)
   