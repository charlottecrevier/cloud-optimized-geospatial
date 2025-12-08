"""
The developers of the pystac-client library provide multiple [examples](https://pystac-client.readthedocs.io/en/latest/tutorials.html) for interacting with
STAC API. Please refer to those and consult the [pystac-client documentation](https://pystac-client.readthedocs.io/en/latest/quickstart.html) for additional information. 

For certificate error while accessing the STAC API, see [using custom certificate](https://pystac-client.readthedocs.io/en/stable/usage.html#using-custom-certificates) documentation

## List collections

In this example you will learn how to query a STAC API with pystac-client to get the available collections
"""
# --8<-- [start:code]
# Import the library needed
import pystac_client

# Link to ccmeo datacube stac-api
stac_root = "https://datacube.services.geo.ca/stac/api"
# Initialize the STAC client
catalog = pystac_client.Client.open(stac_root)

# Get the list of available collection id
for collection in catalog.get_collections():
    print(collection.id)
# --8<-- [end:code]