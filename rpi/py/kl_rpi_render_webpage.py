import kl_rpi_base
import kl_rpi_fileIO

class render_html:
    def __init__(self):
        self.CONFIG        = kl_rpi_base.kl_rpi_config()
        self.fileio        = kl_rpi_fileIO.file_io_three()
        self.file_buffer   = []
        self.LATDD         = 0
        self.LONDD         = 0
        ########################
        self.CONFIG.read_cfg()
        self.outfpath      =  self.CONFIG.ATTR_HTDOCS  #'/var/www'    
        self.outfname      =  self.CONFIG.ATTR_WEBPAGE #'gps_map.html' #   #

        #print ('writing file : '+(self.outfpath +'/'+self.outfname) ) 

   ###################################
    def set_latlon(self,lat,lon):
       self.LATDD = lat
       self.LONDD = lon

   ###################################
    def render(self):
	self.file_buffer.append('<!DOCTYPE HTML>')
	self.file_buffer.append('<html>')
	self.file_buffer.append('  <head>')
	self.file_buffer.append('    <title>RPI GPS DEMO</title>')
	self.file_buffer.append('    <style type="text/css">')
	self.file_buffer.append('      html, body, #basicMap {')
	self.file_buffer.append('          width: 100%;')
	self.file_buffer.append('          height: 100%;')
	self.file_buffer.append('          margin: 0;')
	self.file_buffer.append('      }')
	self.file_buffer.append('    </style>')
	self.file_buffer.append('    <script  src="proj4js/lib/proj4js-compressed.js"        type="text/javascript"></script>')
	self.file_buffer.append('    <script src="open/OpenLayers.js"></script>')
	self.file_buffer.append('    <script>')
	self.file_buffer.append('      function init() {')
	self.file_buffer.append('        map = new OpenLayers.Map("basicMap", {allOverlays: false });')
	self.file_buffer.append('        var markers = new OpenLayers.Layer.Markers( "Markers" );')
	self.file_buffer.append('        map.addLayer(markers);')
	self.file_buffer.append('        var size = new OpenLayers.Size(21,25);')
	self.file_buffer.append('        var offset = new OpenLayers.Pixel(-(size.w/2), -size.h);')
	self.file_buffer.append('        var icon = new OpenLayers.Icon(\'http://www.openlayers.org/dev/img/marker.png\',size,offset);')
	self.file_buffer.append('        markers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat('+str(self.LONDD)+','+str(self.LATDD)+'),icon));')
	self.file_buffer.append('        map.addControl(')
	self.file_buffer.append('                new OpenLayers.Control.MousePosition({')
	self.file_buffer.append('                    prefix: \'<a target="_blank" \' +')
	self.file_buffer.append('                        \'href="http://spatialreference.org/ref/epsg/4326/">\' +')
	self.file_buffer.append('                        \'EPSG:4326</a> coordinates: \',')
	self.file_buffer.append('                    separator: \' | \',')
	self.file_buffer.append('                    numDigits: 2,')
	self.file_buffer.append('                    emptyString: \'Mouse is not over map.\'')
	self.file_buffer.append('                })')
	self.file_buffer.append('            );')
	self.file_buffer.append('        var ol_wms = new OpenLayers.Layer.WMS( "OpenLayers WMS",')
	self.file_buffer.append('                    "http://vmap0.tiles.osgeo.org/wms/vmap0?", {layers: \'basic\'} );')
	self.file_buffer.append('        map.addLayer(ol_wms);')
	self.file_buffer.append('        map.setCenter(new OpenLayers.LonLat('+str(self.LONDD)+','+str(self.LATDD)+'), 5);')
	self.file_buffer.append('      }')
	self.file_buffer.append('    </script>')
	self.file_buffer.append('  </head>')
	self.file_buffer.append('  <body onload="init();">')
	self.file_buffer.append('    <div id="basicMap"></div>')
	self.file_buffer.append('  </body>')
	self.file_buffer.append('</html>')

        #print self.file_buffer
        print ('writing file : '+(self.outfpath    +'/'+self.outfname) ) 
        self.fileio.writefile_list( (self.outfpath +'/'+self.outfname) ,self.file_buffer) 


########################
foo = render_html()
foo.render()

