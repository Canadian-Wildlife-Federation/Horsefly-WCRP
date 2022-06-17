#!/usr/bin/env python
# coding: utf-8

# # API practice

# This is where I will be practice producing API called maps.

# In[1]:


from ipyleaflet import *
import json


#make the map
m = Map(center=(60,-120), zoom=5, basemap = basemaps.Esri.DeLorme)

#add the layers
with open('test1.geojson') as f:
    data = json.load(f)

geo = GeoJSON(data=data,
              style = {
                'color': 'blue'
              })

m.add_layer(geo)

#attempt at querying data from pg_featureserv API for bcfishpass

import requests
import json

query = '?watershed_group_code=BULK'

response_API = requests.get('https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.barriers_bt/items.json'+query)

parse = response_API.text
gjson = json.loads(parse)

geo1 = GeoJSON(data=gjson,
              style = {
                'color': 'black'
              })

m.add_layer(geo1)


m

