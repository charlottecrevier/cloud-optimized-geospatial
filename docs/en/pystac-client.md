# Accessing CCMEO STAC API
Examples on how to use python libraries to discover the
collections from the CCMEO datacube STAC API. 

## Using [pystac-client]

``` sh
--8<-- "how-to-guides/pystac-client-requirements.txt:3:3"
```

The developers of the pystac-client library provide multiple [examples] for interacting with
STAC API. Please refer to those and consult the [pystac-client documentation] for additional information. 

For certificate error while accessing the STAC API, see [using custom certificate] documentation

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

For more details on search parameters available with pystac-client, see [items search] documentation.  

``` py linenums="1"
--8<-- "how-to-guides/pystac-client-items-example.py:code"
```
<!-- END: Get a list of items using pystac-client -->

[pystac-client]: https://github.com/stac-utils/pystac-client
[items search]: https://pystac-client.readthedocs.io/en/stable/usage.html#itemsearch
[using custom certificate]: <https://pystac-client.readthedocs.io/en/stable/usage.html#using-custom-certificates>
[examples]: https://pystac-client.readthedocs.io/en/latest/tutorials.html
[pystac-client documentation]: https://pystac-client.readthedocs.io/en/latest/quickstart.html

*[COG]: Cloud Optimized GeoTIFF
*[STAC]: Spatio-Temporal Asset Catalog
*[CCMEO]: Canada Center for Mapping and Earth Observation, Natural Resources Canada


