from decimal import Decimal
import chardet
import pandas as pd
import re

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

def add_qds(file, latitudeField, longitudeField):
    print('checking file encoding')
    with open(file, 'rb') as f:
        result = chardet.detect(f.read())

    print('reading file')
    df = pd.read_csv(file, encoding=result['encoding'], keep_default_na=False)
    df["QDS"] = None

    print('adding QDSs')
    for index, row in df.iterrows(): 
        #barcode = df_missingQDS.loc[index][0]
        lat = row.loc[latitudeField]
        long = row.loc[longitudeField]
        if lat and long:
            if isinstance(lat, str) and isinstance(long, str):
                try:
                    lat = float(lat)
                    long = float(long)
                except:
                    print(f'could not convert {lat}, {long} in row {index}: invalid format')
                    continue

            # do the conversion
            if lat and long and isinstance(lat, float) and isinstance(long, float):
                try:
                    qds = dd_to_qds(lat, long)
                    df.loc[index, "QDS"] = qds
                except Exception as ex:
                    print(f'could not convert {lat}, {long} in row {index}: {str(ex)}')
                    continue
            else:
                print(f'invalid coordinate format in row {index}')
                continue

        elif lat or long:
            print(f'missing coordinate value in row {index}')
            continue
        else:
            continue

    print('writing out updated file')

    newfile = re.sub(".csv$", '_QDS.csv', file, flags=re.I) 
    df.to_csv(newfile, index = False)

    print('all done...')
   