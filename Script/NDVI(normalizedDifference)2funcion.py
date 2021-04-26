cuencas = ee.FeatureCollection('users/c/Provincias')
APER = cuencas.filter(ee.Filter.eq("NOMPRO","HUAYLAS"))
collection = ee.ImageCollection("LANDSAT/LT05/C01/T1_SR")\
.filter(ee.Filter.eq('WRS_PATH', 8))\
.filter(ee.Filter.eq('WRS_ROW', 66))\
.filterMetadata('CLOUD_COVER' ,'less_than',30)
def ndvi(image):
    return image.normalizedDifference([ 'B4' ,'B3']).rename('NDVI')
ndvi = collection.map(ndvi)
mean = ndvi.mean()

NDVI_TO_EXPORT = mean.clip(APER)
palette = [ 'FFFFFF','CE7E45','DF923D','F18555','FCD163',
'998718','74A901','66A000','529400','3E8601','207401','056201',
'004C00','023801','012E01','011D01','011D01','011301']

Map.addLayer(
NDVI_TO_EXPORT,{'max': 1, 'min': 0, 'palette': palette},'Evapotransl')