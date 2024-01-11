from os import path
from functions import add_qds

#SETTINGS

filepath = r'C:\Users\Ian Engelbrecht\Downloads' #empty string if local directory
filename = r'NU_Senecio_Oct2022_georeferenced20230328.csv'
latitudeField = 'dwc:decimalLatitude'
longitudeField = 'dwc:decimalLongitude'

#SCRIPT
add_qds(path.join(filepath, filename), latitudeField, longitudeField)