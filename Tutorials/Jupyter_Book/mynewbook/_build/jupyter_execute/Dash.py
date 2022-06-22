#!/usr/bin/env python
# coding: utf-8

# # Dash App using Dash-leaflet

# This is a basic app using data called from the api as well as some interactivity.

# In[1]:


import dash
from dash import Dash, dcc, html, Input, Output #pip install dash
import jupyter_dash #integrated in jupyter notebooks
from jupyter_dash import JupyterDash as JD
import dash_leaflet as dl
import dash_leaflet.express as dlx
import requests
import json
from dash_extensions.javascript import assign


# In[2]:


#querying data from pg_featureserv API for bcfishpass
request = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.streams/items.json'
query = '?properties=watershed_group_code,segmented_stream_id&filter=watershed_group_code%20=%20%27HORS%27' #this query slows things down for some reason

request1 = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.crossings/items.json'
query1 = '?filter=watershed_group_code%20=%20%27HORS%27%20AND%20all_spawningrearing_km%3e0'

response_API = requests.get(request+query)
response_API1 = requests.get(request1+query1)

parse = response_API.text
stream = json.loads(parse)

parse1 = response_API1.text
gjson = json.loads(parse1)


# In[3]:


#configuring the app
#useful resources include:
#https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Other/Dash_Introduction/intro.py
#https://dash-leaflet.herokuapp.com/
#https://github.com/plotly/jupyter-dash/blob/master/notebooks/getting_started.ipynb

app = Dash(__name__)

#making dropdown option based on property in data table
id_list = []

features = gjson['features']
for i in range(len(features)):
    lati=features[i]['geometry']['coordinates'][1]
    long=features[i]['geometry']['coordinates'][0]
    cross_id = str(features[i]['id'])

    temp = dict(name = cross_id, lat = lati, lon = long)

    id_list = id_list + [temp,]

dd_options = [dict(value=j['name'], label=j['name']) for j in id_list]
dd_defaults = [o['value'] for o in dd_options]

# print(dd_defaults)
# print(type(dd_defaults[2]))

# # Generate geojson with a marker for each city and name as tooltip.
geojson = dlx.dicts_to_geojson([{**c, **dict(tooltip=c['name'])} for c in id_list])

gjson_filter = assign("function(feature, context){return context.props.hideout.includes(feature.name);}")



# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Web Application Dashboard for Fish Passage BC", style={'text-align': 'center'}),

    dcc.Dropdown(id="dd",
                 options=dd_options,
                 value=dd_defaults,
                 multi=True,
                 style={'width': "40%"}
                 ),
    
    #Map ...use geobuf for faster option in cumputing
    dl.Map(center=[52.6,-120.5], zoom=8, children=[
        dl.TileLayer(),
        dl.GeoJSON(data=stream, id="streams"),
        dl.GeoJSON(data=geojson, options=dict(filter=geojson_filter), hideout=dd_defaults, id="geojson", zoomToBounds=True)
        ]
        ,style={'width': '800px', 'height': '500px'} #style is key as map will not show up without it

    ),

    #html.Div(id='stream'),

    #html.H3(id='cross')

    #html.Div(id='output_container', children=[]),
    #html.Br(),

    #dcc.Graph(id='my_bee_map', figure={}) #add a graph if need be

])

# ------------------------------------------------------------------------------
# Connect Leaflet Map to Dash Components
@app.callback(
   Output('stream', 'children'), [Input('streams', 'click_feature')]
)
def stream_click(feature):
    if feature is not None:
        return f"The stream is {feature['properties']['segmented_stream_id']}"

@app.callback(
    Output('geojson', 'hideout'), [Input('dd', 'value')]
)
def cross_click(feature):
    return feature

#app.clientside_callback("function(x){return x;}", Output("crossings", "hideout"), Input("TableValue", "value"))

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server()

