import gdal
import json
from os import remove
from tempfile import NamedTemporaryFile


def format_handler(**kwargs):
    headers_ = kwargs["headers_"]
    dataset = kwargs["dataset"]
    geojson = json.dumps(kwargs["content"], default=kwargs["json_serial"])
    headers_["Content-Type"] = "application/x-sqlite3"
    headers_["Content-Disposition"] = 'attachment; filename="{}.gpkg'.format(dataset)
    content = geojson2gpkg(geojson, dataset)
    return headers_, 200, content


def geojson2gpkg(geojson, tablename="items"):
    dsi = gdal.OpenEx(geojson)
    layer = dsi.GetLayer()
    tempfile_instance = NamedTemporaryFile("r", suffix="gpkg")
    temp_filename = tempfile_instance.name
    tempfile_instance.close()
    drv = gdal.GetDriverByName("GPKG")
    gpkg_filename = temp_filename + ".gpkg"
    dso = drv.Create(gpkg_filename, 0, 0, 0, gdal.GDT_Unknown)
    dso.CopyLayer(layer, tablename)
    gpkg_file = open(gpkg_filename, "rb")
    content = gpkg_file.read()
    remove(gpkg_filename)
    return content
