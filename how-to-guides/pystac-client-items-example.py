"""
## List items

In this example you will learn how to :   

- Query a STAC API with pystac-client with a portion of filter;   
- Access the data href for the specific filter.  

!!! info
    This specific example uses the collection hrdem-mosaic-2m from CCMEO's datacube

For more details on search parameters available with pystac-client, see [items search](https://pystac-client.readthedocs.io/en/stable/usage.html#itemsearch) documentation.  
"""
# --8<-- [start:code]
# Import the library needed
import pystac_client

# Link to ccmeo datacube stac-api
stac_root = "https://datacube.services.geo.ca/stac/api"
# Initialize the STAC client
catalog = pystac_client.Client.open(stac_root)

# Define search parameters
# In this example, we filter on the mosaic collection of HRDEM tiles
collections = ['hrdem-mosaic-2m']
# We define a bounding box extent
extent = [-79.28229773059192, 44.31501485755303, 
		  -79.1702187573089, 44.3929540402247]

# Build the search query with the filtering parameters
search = catalog.search(
	collections=collections, 
	bbox=extent
	) 

# Use the pagination to improve efficiency
links=[]
# Iterate over each returned page and get the dtm COG link
for page in search.pages():
	for item in page:
		links.append(item.assets['dtm'].href)
# --8<-- [end:code]