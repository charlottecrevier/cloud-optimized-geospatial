"""
The developers of the rasterio library provide additional examples of usage. 
For more details on the rasterio library, see the [rasterio](https://rasterio.readthedocs.io/en/latest/quickstart.html) documentation.

## Read the header of a remote COG

In this code you will : 

- Query a STAC API with pystac-client to get link to a COG;  
- Read header metadata from a remote COG file

!!! info
    This specific example uses the collection **mrdem-30** from CCMEO's datacube
"""
# --8<-- [start:code]
import pystac_client
import rasterio 

# Define a bounding box for an AOI (Ottawa) in EPSG:4326
bbox = [-75.8860,45.3157,-75.5261,45.5142]
bbox_crs = "EPSG:4326"

# Link to ccmeo datacube stac-api
stac_root = "https://datacube.services.geo.ca/stac/api"
catalog = pystac_client.Client.open(stac_root)

search = catalog.search(
	collections=['mrdem-30'], 
    bbox=bbox,
	) 

# Get the link to the data asset for mrdem-30 dtm
links = []
for page in search.pages():
	for item in page:
		links.append(item.assets['dtm'].href)

# Read the header of a remote COG 
with rasterio.open(links[0]) as src:
    # Read the header of a COG
    print(src.tags())
    # >> {'AREA_OR_POINT': 'Area', 
    #     'TIFFTAG_DATETIME': '2024:06:13 12:00:00'}
    print(src.profile)
    # >> {'driver': 'GTiff', 'dtype': 'float32', 'nodata': -32767.0, 
    #   'width': 183687, 'height': 159655, 'count': 1, 
    #   'crs': CRS.from_epsg(3979), 'transform': Affine(30.0, 0.0, 
    #   -2454000.0, 0.0, -30.0, 3887400.0), 'blockxsize': 512, 
    #   'blockysize': 512, 'tiled': True, 'compress': 'lzw', 
    #   'interleave': 'band'}
# --8<-- [end:code]




