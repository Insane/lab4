import arcpy
import numpy
tablica1=arcpy.da.FeatureClassToNumPyArray("powiaty","POLE_KM2")
tablica2=arcpy.da.FeatureClassToNumPyArray("powiaty","POP")
numpy.corrcoef(tablica1,tablica2)

