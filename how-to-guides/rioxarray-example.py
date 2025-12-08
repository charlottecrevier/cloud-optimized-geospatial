"""
Load a single COG, using the link to the s3 object, into an xarray.

Rioxarray is based on rasterio, and can be used to read data into Xarray object. 
The developers of the rioxarray library provide additional usage examples, 
like this [one](https://corteva.github.io/rioxarray/stable/examples/read-locks.html).

## Read a portion of a remote COG into an xarray

In this code you will : 

- Query a STAC API with pystac-client to get link to a COG;  
- Use rioxarray to read header of remote COG;
- Open the remote COG by chunks;
- Read an area of interest into an in memory Xarray object

!!! info
    This specific example uses the collection **hrdem-lidar** from CCMEO's datacube

!!! Warning 
    By default, the bbox used for clipping data inside `rio.clip_bbox()` needs to be in 
    the projected coordinate system.  
    See <https://corteva.github.io/rioxarray/stable/examples/clip_box.html#Clip-using-a-bounding-box>

!!! Note 
    When using `rioxarray.open_rasterio()` set `chunks` to enable lazy loading with Dask. This allows 
    Dask to read data in smaller chunks, improving speed and memory usage through parallel computing. 
    For example, a `chunk` size of 1000 for both x and y means Dask reads 100x100 boxes instead of the 
    entire array, processing multiple chunks simultaneously.
"""
# --8<-- [start:code]
import pystac_client
import rioxarray

bbox=[-75.8860,45.3157,-75.5261,45.5142] 
bbox_crs = "EPSG:4326"

# Link to ccmeo datacube stac-api
stac_root = "https://datacube.services.geo.ca/stac/api"
# Initialize the STAC client
catalog = pystac_client.Client.open(stac_root)

search = catalog.search(
	collections=['mrdem-30'], 
    bbox=bbox,
	) 

# Use the rioxarray.open_rasterio() and clip it to the bbox
for page in search.pages():
    for item in page:
        band = rioxarray.open_rasterio(
            item.assets['dtm'].href, 
            chunks=512,
            ).rio.clip_box(*bbox,crs=bbox_crs)

# At this point the data is not read in the Xarray object
# See the Xarray object details
print(band)
# <xarray.DataArray (band: 1, y: 999, x: 1134)> Size: 5MB
# dask.array<getitem, shape=(1, 999, 1134), dtype=float32, chunksize=(1, 512, 512), chunktype=numpy.ndarray>
# Coordinates:
#   * band         (band) int64 8B 1
#   * x            (x) float64 9kB 1.493e+06 1.493e+06 ... 1.527e+06 1.527e+06
#   * y            (y) float64 8kB -1.557e+05 -1.558e+05 ... -1.857e+05 -1.857e+05
#     spatial_ref  int64 8B 0
# Attributes:
#     TIFFTAG_DATETIME:  2024:12:12 12:00:00
#     AREA_OR_POINT:     Area
#     scale_factor:      1.0
#     add_offset:        0.0
#     _FillValue:        -32767.0

# At this point, the metadata and array shape are set, but the data itself isn't read.
# Running .compute() allows Dask to optimize the workflow, evaluating and executing it 
# in the most efficient way, optimizing resource usage.

# Perform analysis...

# To read the data
band.compute()
# --8<-- [end:code]



