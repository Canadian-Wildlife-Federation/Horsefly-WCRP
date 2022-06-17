#!/usr/bin/env python
# coding: utf-8

# # API practice

# This is where I will be practice producing API called maps.

# In[1]:


from ipyleaflet import *
import json


#make the map
m = Map(center=(50,-120), zoom=6, basemap = basemaps.Esri.DeLorme)

#add the layers
with open('test.geojson') as f:
    data = json.load(f)

geo = GeoJSON(data=data,
              style = {
                'color': 'blue'
              })

m.add_layer(geo)

# #attempt at querying data from pg_featureserv API for bcfishpass

# import requests
# import json

# response_API = requests.get('https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.streams/items.json')
# print(response_API.status_code)

# parse = response_API.text
# gjson = json.loads(parse)

# geo1 = GeoJSON(data=gjson,
#               style = {
#                 'color': 'blue'
#               })

# m.add_layer(geo1)


m


# In[43]:


#attempt at querying data from pg_featureserv API for bcfishpass

import requests
import json

response_API = requests.get('https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.streams/items.json')
print(response_API.status_code)

data = response_API.text
json.loads(data)


