# Accessing CCMEO STAC API
Examples on how to use python libraries to discover the
collections from the CCMEO datacube STAC API. 

## Using [pystac-client]

``` sh
--8<-- "how-to-guides/pystac-client-requirements.txt:3:3"
```

<!-- START: Get a list of collections using pystac-client -->
::: how-to-guides.pystac-client-collections-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC


``` py linenums="1"
--8<-- "how-to-guides/pystac-client-collections-example.py:code"
```
<!-- END: Get a list of collections using pystac-client -->

<!-- START: Get a list of items using pystac-client -->
::: how-to-guides.pystac-client-items-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC


``` py linenums="1"
--8<-- "how-to-guides/pystac-client-items-example.py:code"
```
<!-- END: Get a list of items using pystac-client -->

[pystac-client]: https://github.com/stac-utils/pystac-client

*[COG]: Cloud Optimized GeoTIFF
*[STAC]: Spatio-Temporal Asset Catalog
*[CCMEO]: Canada Center for Mapping and Earth Observation, Natural Resources Canada


