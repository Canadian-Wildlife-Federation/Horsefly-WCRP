#!/usr/bin/env python
# coding: utf-8

# # Dash App using Dash-leaflet

# This is a basic app using data called from the api as well as some interactivity.

# In[1]:


import dash
from dash import Dash, dcc, html, Input, Output, dash_table #pip install dash
import jupyter_dash #integrated in jupyter notebooks
from jupyter_dash import JupyterDash as JD
import dash_leaflet as dl
import dash_leaflet.express as dlx
import requests
import json
from dash_extensions.javascript import assign
import pandas as pd
import geopandas as gpd
import numpy as np


# In[2]:


#querying data from pg_featureserv API for bcfishpass
request = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.streams/items.json'
query = '?properties=watershed_group_code,segmented_stream_id&filter=watershed_group_code%20=%20%27HORS%27' #this query slows things down for some reason

request1 = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.crossings/items.json'
query1 = '?properties=aggregated_crossings_id,pscis_status,barrier_status,access_model_ch_co_sk,all_spawningrearing_per_barrier,all_spawningrearing_km&filter=watershed_group_code%20=%20%27HORS%27%20AND%20all_spawningrearing_km%3e0'

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

app =Dash(__name__)

#making dropdown option based on property in data table
id_list = []

#priority vs intermediate barrier list
prior_table = pd.read_csv('tables\priority_barriers.csv', index_col=False)

#seperate GeoJSOn for selected filtering


features = gjson['features']
for i in range(len(features)):
    pscis=features[i]['properties']['pscis_status']
    barr=features[i]['properties']['barrier_status']
    acc=features[i]['properties']['access_model_ch_co_sk']
    all=features[i]['properties']['all_spawningrearing_per_barrier']
    cross_id = str(features[i]['properties']['aggregated_crossings_id'])

    temp = dict(id = cross_id, pscis_status=pscis, barrier_status=barr, access_model_ch_co_sk=acc, all_spawningrearing_per_barrier=all)

    id_list = id_list + [temp,]

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Web Application Dashboard for Fish Passage BC", style={'text-align': 'left'}),

    dcc.Dropdown(
        options=[
            {'label': 'Priority Barrier List', 'value': 'priority'},
            {'label': 'Intermediate Barrier List', 'value': 'intermediate'}
        ],
        id='dd',
        style={'width': '1000px'}
    ),

    html.Br(),

    dash_table.DataTable(data=[],
                        style_data={
                            'color': 'white',
                            'backgroundColor': 'black'
                        },
                        style_table={'float':'left','width': '1000px'},
                        id='table2',
                        active_cell= None
                        ),
    
    html.Button('Default View', id='home', n_clicks=0),
    
    

    dl.Map(center=[52.6,-120.5], zoom=8, children=[
        
        
        dl.LayersControl(
        [dl.BaseLayer(dl.TileLayer(url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                    attribution='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'), name='ESRI Topographic', checked=False),
                    dl.BaseLayer(dl.TileLayer(), name='Base', checked=True)] +
        [dl.Overlay(dl.GeoJSON(data=stream, id="streams"), name='Streams',checked=True),
        dl.Overlay(dl.GeoJSON(data=gjson, zoomToBounds=True, zoomToBoundsOnClick=True, id="cross", cluster=True), name='Crossings',checked=True)]
        )
        ]
        ,style={'width': '1000px', 'height': '500px'}, #style is key as map will not show up without it
        id='map'
    ),

    dash_table.DataTable(data=[],
                        style_data={
                            'color': 'white',
                            'backgroundColor': 'black'
                        },
                        style_table={'float':'left','width': '1000px'},
                        id='table'
                        ),

    html.Div(id='test')



])



# ------------------------------------------------------------------------------
# Connect Leaflet Map to Dash Components
@app.callback(
   Output('table', 'data'),
    [Input('cross', 'click_feature')]
)
def update_table(feature):
    if feature is not None:
        id_index = dict((p['id'],i) for i,p in enumerate(id_list))
        index = id_index.get(feature['id'], -1)
        data = [id_list[index]]
        return data
    return dash.no_update

@app.callback(
   Output('table2', 'data'),
    [Input('dd', 'value')]
)
def update_table2(table_value):
    data = []
    if table_value == 'intermediate':
        for i in range(0, len(prior_table.iloc[:,1])):
            id_index = dict((p['id'],j) for j,p in enumerate(id_list))
            index1 = id_index.get(str(prior_table.iloc[:,0][i]), -1)
            data = data + [id_list[index1],]
    elif table_value == 'priority':
        for i in range(0, len(prior_table.iloc[:,0])):
            id_index = dict((p['id'],j) for j,p in enumerate(id_list))
            index1 = id_index.get(str(prior_table.iloc[:,1][i]), -1)
            data = data + [id_list[index1],]
    
    return data

@app.callback(
    Output('cross', 'data'), [Input('table2', 'active_cell'), Input('dd', 'value')]
)
def marker(cell, value):
    if value == 'intermediate':
        if cell['column_id'] == "id":
            geojson = json.loads(parse1)
            features = geojson.pop('features')
            geojson['features'] = []
            for i in features:
                if str(i['properties']['aggregated_crossings_id']) == cell['row_id']:
                    geojson['features'].append(i)
                    return geojson
    elif value == 'priority':
        if cell['column_id'] == "id":
            geojson = json.loads(parse1)
            features = geojson.pop('features')
            geojson['features'] = []
            for i in features:
                if str(i['properties']['aggregated_crossings_id']) == cell['row_id']:
                    geojson['features'].append(i)
                    return geojson
    else:
        return dash.no_update

# @app.callback(
#     Output('cross', 'data'), [Input('home', 'n_clicks')]
# )
# def update_map(view):
#     return gjson
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server()

