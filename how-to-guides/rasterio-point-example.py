"""
## Read a portion of a remote COG - Point

For this example, you will need to also install [shapely](https://shapely.readthedocs.io/en/stable/installation.html):   
```bash
pip install shapely
```

In this code you will : 

- Query a STAC API with pystac-client;
- Read values of remote COG based on coordinates with the sample functionality;

!!! info
    This specific example uses the collection **mrdem-30** from CCMEO's datacube

!!! Tip
    The pixel value closest to the coordinate will be return by the sample() function. 
    No interpolation is performed
    
    API definition: <https://rasterio.readthedocs.io/en/stable/api/rasterio.io.html#rasterio.io.DatasetReader.sample>
"""
# --8<-- [start:code]
import pystac_client
import rasterio 
import pyproj
from shapely.geometry import Point
from shapely.ops import transform


# Define the coordinate of the point of interest in EPSG:4326 (for the request to the STAC API)
lonlat = Point(-104.898838, 69.232434)

# Modify the projection of the point (for the COG extraction)
proj = pyproj.Transformer.from_crs(4326, 3979, always_xy=True)
point =  transform(proj.transform, lonlat)
x1, y1 = point.coords.xy


# Link to ccmeo datacube stac-api
stac_root = "https://datacube.services.geo.ca/stac/api"
catalog = pystac_client.Client.open(stac_root)

search = catalog.search(
	collections=['mrdem-30'], 
    intersects=lonlat,
	) 

# Get the link to the data asset for mrdem-30 dtm and dsm
links = {}
for page in search.pages():
	for item in page:
		links['dtm'] = item.assets['dtm'].href
		links['dsm'] = item.assets['dsm'].href

# Read value from coordinates
for asset, href in links.items():
    with rasterio.open(href) as src:
        for val in src.sample([(x1, y1)]): 
            print(f'{asset} : {val}')
   
# --8<-- [end:code]




