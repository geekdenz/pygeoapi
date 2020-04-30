from pygeoapi import __version__
HEADERS = {
    'Content-Type': 'application/json',
    'X-Powered-By': 'pygeoapi {}'.format(__version__)
}
def get_collection_items(func, *args, **kwargs):
    print('geopackage.get_collection_items() called')
    # return func(*args, **kwargs)
    # return 'Hello GeoPackge'
    headers_ = HEADERS.copy()
    headers_['Content-Type'] = 'text/html'
    return headers_, 200, 'Hello GPKG'