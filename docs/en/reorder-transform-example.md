# Re-Order the STAC proj:Transform

This is a known issue in the STAC metadata. Will be fixed in the future. 
In the mean time, this is the suggested fix. 

!!! Warning
    
    This is needed when using **odc-stac** and **stackstac** libraries, which are based on GDAL. 

`GDAL GetGeoTransform` and `rasterio` use different formats for transform metadata. The order expected in the STAC `proj:transform` is the same as reported by `rasterio`. When using GDAL method you need to re-order the `proj:transform`
coming from the STAC metadata to be able to load the pystac object into xarray automatically. 

``` py
--8<-- "how-to-guides/odc-stac-example.py:transform"
```
     
For more information, please see [STAC documentation on proj:transform]

[STAC documentation on proj:transform]:  https://github.com/stac-extensions/projection?tab=readme-ov-file#projtransform

*[STAC]: Spatio-Temporal Asset Catalog