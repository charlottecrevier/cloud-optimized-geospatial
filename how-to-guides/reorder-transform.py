"""
# Re-Order the STAC proj:Transform

This is a known issue in the STAC metadata. Will be fixed in the future. 
In the mean time, this is the suggested fix. 

!!! Warning
    
    This is needed when using **odc-stac** and **stackstac** libraries, which are based on GDAL. 

`GDAL GetGeoTransform` and `rasterio` use different formats for transform metadata. The order expected in the STAC `proj:transform` is the same as reported by `rasterio`. When using GDAL method you need to re-order the `proj:transform`
coming from the STAC metadata to be able to load the pystac object into xarray automatically.

For more information, please see [STAC documentation on proj:transform](https://github.com/stac-extensions/projection?tab=readme-ov-file#projtransform)
"""
# --8<-- [start:transform]
def reorder_transform(gdal_transform):
    """
    Reorders the GDAL GeoTransform (6-element tuple) into the 9-element format
    that is compatible with proj:transform.
    """
    return [gdal_transform[1], gdal_transform[2], gdal_transform[0],
            gdal_transform[4], gdal_transform[5], gdal_transform[3],
            0, 0, 1]
# --8<-- [end:transform]