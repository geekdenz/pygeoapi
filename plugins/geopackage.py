from pygeoapi.formatter.formatters import register
from pygeoapi.formatter.base import BaseFormatter
from pygeoapi.util import json_serial
import json

class GeopackageFormatter:
    def handle(self, headers_, content, default=json_serial):
        # headers_['Content-Type'] = 'text/html'
        print('handled by GeopackageFormatter')
        return headers_, 200, json.dumps(content, default=json_serial)


register('geopackage', GeopackageFormatter)