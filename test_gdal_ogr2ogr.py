# import gdaltools as g

# unicode = str
# info = g.ogrinfo('luc002.gpkg')
# print(info)
import gdal
from gdal import ogr

drv = gdal.GetDriverByName("GPKG")
dso = drv.Create("luc_from_py.gpkg", 0, 0, 0, gdal.GDT_Unknown)

pgdrv = gdal.GetDriverByName("PostgreSQL")
# pgds = pgdrv.OpenEx("host='heuert-postgis' dbname='luc' user='pygeoapi' password='pygeoapi'")
pgds = gdal.OpenEx(
    "PG:host='heuert-postgis' dbname='luc' user='pygeoapi' password='pygeoapi'",
    gdal.OF_VECTOR,
)
pglayer = pgds.ExecuteSQL(
    "select fid as ogc_fid, geom, luc from nzlri_land_use_capability_wgs84 limit 13"
)
dso.CopyLayer(pglayer, "luc_new")
