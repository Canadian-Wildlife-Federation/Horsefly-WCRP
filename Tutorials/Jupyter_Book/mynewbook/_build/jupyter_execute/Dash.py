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
import dash_leaflet.express as dlx #pip install --upgrade protobuf==3.20.0 --user before importing and if necessarym, restart the kernel
import requests
import json
from dash_extensions.javascript import assign, arrow_function
import pandas as pd
#import geopandas as gpd
import numpy as np
import random
from flask_caching import Cache
import os
import dash_bootstrap_components as dbc


# In[2]:


# #querying data from pg_featureserv API for bcfishpass
request = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.streams/items.json'
query = '?properties=watershed_group_code,segmented_stream_id&filter=watershed_group_code%20=%20%27HORS%27' #this query slows things down for some reason

request1 = 'https://tiles.hillcrestgeo.ca/bcfishpass/bcfishpass.streams.json'
query1 = '?properties=watershed_group_code,segmented_stream_id&filter=watershed_group_code%20=%20%27HORS%27'

response_API = requests.get(request+query)
response_API1 = requests.get(request1+query1)

parse = response_API.text
stream = json.loads(parse)

parse1 = response_API1.text
gjson = json.loads(parse1)

# #api call function
# def apiCall(w):
#     request = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.streams/items.json'
#     query = '?properties=watershed_group_code,segmented_stream_id&filter=watershed_group_code%20=%20%27' + w + '%27' #this query slows things down for some reason

#     request1 = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.crossings/items.json'
#     query1 = '?properties=aggregated_crossings_id,pscis_status,barrier_status,access_model_ch_co_sk,all_spawningrearing_per_barrier,all_spawningrearing_km&filter=watershed_group_code%20=%20%27' + w + '%27%20AND%20all_spawningrearing_km%3e0'

#     response_API = requests.get(request+query)
#     response_API1 = requests.get(request1+query1)

#     parse = response_API.text
#     parse1 = response_API1.text

#     return parse, parse1


# prior_table = pd.read_csv('tables\priority_barriers.csv', index_col=False)
# inter_table = pd.read_csv('tables\inter_barriers.csv', index_col=False)


# In[3]:


# #configuring the app
# #useful resources include:
# #https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Other/Dash_Introduction/intro.py
# #https://dash-leaflet.herokuapp.com/
# #https://github.com/plotly/jupyter-dash/blob/master/notebooks/getting_started.ipynb

# app =JD(__name__)

# #making dropdown option based on property in data table
# id_list = []

# #priority vs intermediate barrier list
# #-------------------------------------------------------------------------------
# #certain barriers in the priority list need to be looked at
# #1100000243 does not show up in API call...no dam 
# #1100000814 is a beaver dam
# #1006800487 is a skid trail that has a low habitat value assessment
# #1100001822 remanents of earthen dam wiyth very low habitat value due to lack of defined channel

# prior_table = pd.read_csv('tables\priority_barriers.csv', index_col=False)
# inter_table = pd.read_csv('tables\inter_barriers.csv', index_col=False)

# #seperate GeoJSOn for selected filtering

# #
# features = gjson['features']
# for i in range(len(features)):
#     pscis=features[i]['properties']['pscis_status']
#     barr=features[i]['properties']['barrier_status']
#     acc=features[i]['properties']['access_model_ch_co_sk']
#     all=features[i]['properties']['all_spawningrearing_per_barrier']
#     cross_id = str(features[i]['properties']['aggregated_crossings_id'])

#     temp = dict(id = cross_id, pscis_status=pscis, barrier_status=barr, access_model_ch_co_sk=acc, all_spawningrearing_per_barrier=all)

#     id_list = id_list + [temp,]

# #point to layer 
# point_to_layer = assign("""function(feature, context){
#     return L.circleMarker(feature.coordinates);
# }""")
# # ------------------------------------------------------------------------------
# # App layout
# app.layout = html.Div([

#     html.H1("Web Application Dashboard for Fish Passage BC", style={'text-align': 'left'}),

    

#     dcc.Dropdown(
#         options=[
#             {'label': 'HORS', 'value': 'HORS'},
#             {'label': 'BULK', 'value': 'BULK'},
#             {'label': 'LNIC', 'value': 'LNIC'},
#             {'label': 'ELKR', 'value': 'ELKR'}
#         ],
#         value = 'BULK',
#         id='watershed',
#         style={'width': '1000px'}
#     ),

    
    
#     # html.Button('Default View', id='home', n_clicks=0),
    
    

#     dl.Map(center=[52.6,-120.5], zoom=8, children=[
        
        
#         dl.LayersControl(
#         [dl.BaseLayer(dl.TileLayer(url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
#                     attribution='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'), name='ESRI Topographic', checked=False),
#                     dl.BaseLayer(dl.TileLayer(), name='Base', checked=True)] +
#         [dl.Overlay(dl.GeoJSON(data=stream, id="streams"), name='Streams',checked=True),
#         dl.Overlay(dl.GeoJSON(data=gjson, zoomToBounds=True, zoomToBoundsOnClick=True, id="cross", cluster=True, hoverStyle=arrow_function(dict(weight=5, color='#666'))), name='Crossings',checked=True)]
#         )
#         ]
#         ,style={'width': '1000px', 'height': '500px'}, #style is key as map will not show up without it
#         id='map'
#     ),

#     dcc.Dropdown(
#         options=[
#             {'label': 'Priority Barrier List', 'value': 'priority'},
#             {'label': 'Intermediate Barrier List', 'value': 'intermediate'}
#         ],
#         id='dd',
#         style={'width': '1000px'}
#     ),

#     dash_table.DataTable(data=[],
#                         style_data={
#                             'color': 'white',
#                             'backgroundColor': 'black'
#                         },
#                         style_table={'float':'left','width': '1000px'},
#                         id='table2',
#                         active_cell= None
#                         ),

#     dash_table.DataTable(data=[],
#                         style_data={
#                             'color': 'white',
#                             'backgroundColor': 'black'
#                         },
#                         style_table={'float':'left','width': '1000px'},
#                         id='table'
#                         )



# ])



# # ------------------------------------------------------------------------------
# # Connect Leaflet Map to Dash Components
# @app.callback(
#     [Output('cross', 'data'), Output('streams', 'data')], [Input('watershed', 'value')]
# )
# def update_map(value):
    
    
#     if value == 'BULK':
#         parse, parse1 = apiCall('BULK')
#         B_gjson = json.loads(parse1)
#         B_stream = json.loads(parse)
#         return B_gjson, B_stream
#     elif value == 'LNIC':
#         parse, parse1 = apiCall('LNIC')
#         B_gjson = json.loads(parse1)
#         B_stream = json.loads(parse)
#         return B_gjson, B_stream
#     elif value == 'ELKR':
#         parse, parse1 = apiCall('ELKR')
#         B_gjson = json.loads(parse1)
#         B_stream = json.loads(parse)
#         return B_gjson, B_stream
#     elif value == 'HORS':
#         parse, parse1 = apiCall('HORS')
#         B_gjson = json.loads(parse1)
#         B_stream = json.loads(parse)
#         return B_gjson, B_stream
    
#     else: 
#         return dash.no_update, dash.no_update


# # @app.callback(
# #    Output('table', 'data'),
# #     [Input('cross', 'click_feature')]
# # )
# # def update_table(feature):
# #     if feature is not None:
# #         id_index = dict((p['id'],i) for i,p in enumerate(id_list))
# #         index = id_index.get(feature['id'], -1)
# #         data = [id_list[index]]
# #         return data
# #     return dash.no_update

# # @app.callback(
# #    Output('table2', 'data'),
# #     [Input('dd', 'value')]
# # )
# # def update_table2(table_value):
# #     data = []
# #     if table_value == 'intermediate':
# #         for i in range(0, len(inter_table.iloc[:,0])):
# #             id_index = dict((p['id'],j) for j,p in enumerate(id_list))
# #             index1 = id_index.get(str(inter_table.iloc[:,0][i]), -1)
# #             data = data + [id_list[index1],]
# #     elif table_value == 'priority':
# #         for i in range(0, len(prior_table.iloc[:,0])):
# #             id_index = dict((p['id'],j) for j,p in enumerate(id_list))
# #             index1 = id_index.get(str(prior_table.iloc[:,0][i]), -1)
# #             data = data + [id_list[index1],]
# #     else:
# #         data = id_list
    
# #     return data

# # @app.callback(
# #     Output('cross', 'data'), [Input('table2', 'active_cell'), Input('dd', 'value')]
# # )
# # def marker(cell, value):
# #     if value == 'intermediate':
# #         if cell['column_id'] == "id":
# #             geojson = json.loads(parse1)
# #             features = geojson.pop('features')
# #             geojson['features'] = []
# #             for i in features:
# #                 if str(i['properties']['aggregated_crossings_id']) == cell['row_id']:
# #                     geojson['features'].append(i)
# #                     return geojson
# #     elif value == 'priority':
# #         if cell['column_id'] == "id":
# #             geojson = json.loads(parse1)
# #             features = geojson.pop('features')
# #             geojson['features'] = []
# #             for i in features:
# #                 if str(i['properties']['aggregated_crossings_id']) == cell['row_id']:
# #                     geojson['features'].append(i)
# #                     return geojson
# #     else:
# #         return dash.no_update

# # @app.callback(
# #     Output('cross', 'data'), [Input('home', 'n_clicks')]
# # )
# # def update_map(view):
# #     return gjson
# # ------------------------------------------------------------------------------
# if __name__ == '__main__':
#     app.run_server(mode='inline', port = random.choice(range(2000, 10000)))


# In[4]:


#configuring the app
#useful resources include:
#https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Other/Dash_Introduction/intro.py
#https://dash-leaflet.herokuapp.com/
#https://github.com/plotly/jupyter-dash/blob/master/notebooks/getting_started.ipynb

app =JD(__name__)
cache = Cache()
cache.init_app(app.server, config={'CACHE_TYPE': 'SimpleCache'})
timeout = 20
#making dropdown option based on property in data table
id_list = []

#priority vs intermediate barrier list
#-------------------------------------------------------------------------------
#certain barriers in the priority list need to be looked at
#1100000243 does not show up in API call...no dam 
#1100000814 is a beaver dam
#1006800487 is a skid trail that has a low habitat value assessment
#1100001822 remanents of earthen dam wiyth very low habitat value due to lack of defined channel

prior_table = pd.read_csv('tables\priority_barriers.csv', index_col=False)
inter_table = pd.read_csv('tables\inter_barriers.csv', index_col=False)

#seperate GeoJSOn for selected filtering


# # features = gjson['features']
# def get_tabledata(features):
#     id_list = []
#     for i in range(len(features)):
#         pscis=features[i]['properties']['pscis_status']
#         barr=features[i]['properties']['barrier_status']
#         acc=features[i]['properties']['access_model_ch_co_sk']
#         all=features[i]['properties']['all_spawningrearing_per_barrier']
#         cross_id = str(features[i]['properties']['aggregated_crossings_id'])
#         lat = features[i]['geometry']['coordinates'][1]
#         lon = features[i]['geometry']['coordinates'][0]

#         temp = dict(id = cross_id, pscis_status=pscis, barrier_status=barr, access_model_ch_co_sk=acc, all_spawningrearing_per_barrier=all, lat = lat, lon = lon)

#         id_list = id_list + [temp,]
#     return id_list

# # geojson = dlx.dicts_to_geojson([{**c, **dict(tooltip=c['id'])} for c in id_list])
# # geobuf = dlx.geojson_to_geobuf(geojson)

# #marker cluster group 
# #----------------------------------------------------------------------------------------------------------------------------------

# def get_data(features):
#     accessible = []
#     other = []
#     for i in range(len(features)):
#         if features[i]['properties']['access_model_ch_co_sk'] == 'ACCESSIBLE':
#             accessible.append(
#                 dl.CircleMarker(
#                     color='white',
#                     fillColor = '#32cd32',
#                     fillOpacity = 1, 
#                     center = (features[i]['geometry']['coordinates'][1], features[i]['geometry']['coordinates'][0]), 
#                     children=[
#                         dl.Tooltip(str(features[i]['properties']['aggregated_crossings_id'])),
#                         dl.Popup(str(features[i]['properties']['aggregated_crossings_id'])),
#                     ],
#                 )
#             )
#         else:
#             other.append(
#                 dl.CircleMarker(
#                     color = 'white',
#                     fillColor = '#965ab3',
#                     fillOpacity = 1,
#                     center = (features[i]['geometry']['coordinates'][1], features[i]['geometry']['coordinates'][0]), 
#                     children=[
#                         dl.Tooltip(str(features[i]['properties']['aggregated_crossings_id'])),
#                         dl.Popup()
#                     ],
#                 )
#             )

#     cluster = dl.MarkerClusterGroup(id='markers', children=accessible)
#     other = dl.MarkerClusterGroup(id='markers1', children=other)
#     return cluster,other



 
    #-----------------------------------------------------------------------------------------------------------------------------------

# #point to layer 
# point_to_layer = assign("function(feature, latlng, context){return L.circleMarker(latlng);}")
# ------------------------------------------------------------------------------
prior_drop =  dcc.Dropdown(
                    options=[
                        {'label': 'Priority Barrier List', 'value': 'priority'},
                        {'label': 'Intermediate Barrier List', 'value': 'intermediate'}
                    ],
                    id='dd',
                    style={'width': '500px'}
                )

watershed_drop = dcc.Dropdown(
                    options=[
                        {'label': 'HORS', 'value': 'HORS'},
                        {'label': 'BULK', 'value': 'BULK'},
                        {'label': 'LNIC', 'value': 'LNIC'},
                        {'label': 'ELKR', 'value': 'ELKR'}
                    ],
                    value = 'HORS',
                    id='watershed',
                    style={'width': '500px'}
                )
# App layout
app.layout = html.Div([

    html.H1("Web Application Dashboard for Fish Passage BC", style={'text-align': 'left'}),

    

    dbc.Row([
        dbc.Col(prior_drop, width = 2),
        dbc.Col(watershed_drop, width = 2)
    ], style={'width':'1500px'}),
    
    

    dl.Map(children=[
        
        
        dl.LayersControl(
        [dl.BaseLayer(dl.TileLayer(url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                    attribution='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'), name='ESRI Topographic', checked=False),
                    dl.BaseLayer(dl.TileLayer(), name='Base', checked=True), dl.BaseLayer(dl.TileLayer(url='https://tiles.hillcrestgeo.ca/bcfishpass/bcfishpass.streams/{z}/{x}/{y}.pbf'))] +
        [ dl.Overlay(children=[], checked=True, id='pass', name='Passable')]+
        [ dl.Overlay(children=[], checked=True, id='pot', name='Potential')]+
        [ dl.Overlay(children=[], checked=True, id='bar', name='Barrier')]+
        [ dl.Overlay(children=[], checked=True, id='other', name='Unknown')] +
        [dl.Overlay(dl.GeoJSON(data=stream, id="streams", zoomToBounds=True), name='Stream Network',checked=True)])
        ],
        id='map',
        style={'width': '1500px', 'height': '500px'}, #style is key as map will not show up without it
        center=[52.6,-120.5],
        zoom=8 
    ),


    dash_table.DataTable(
                        columns=[
                            {'name': 'Crossing ID', 'id': 'id', 'type': 'numeric'},
                            {'name': 'PSCIS status', 'id': 'pscis_status', 'type': 'text'},
                            {'name': 'Barrier Status', 'id': 'barrier_status', 'type': 'text'},
                            {'name': 'Acess Model', 'id': 'access_model_ch_co_sk', 'type': 'text'},
                            {'name': 'All habitat', 'id': 'all_spawningrearing_per_barrier', 'type': 'numeric'},
                            {'name': 'Latitude', 'id': 'lat', 'type': 'numeric'},
                            {'name': 'Longitude', 'id': 'lon', 'type': 'numeric'}
                        ],
                        data=[],
                        sort_action="native",
                        sort_mode="multi",
                        filter_action="native",
                        style_data={
                            'color': 'white',
                            'backgroundColor': 'black'
                        },
                        style_table={'float':'left','width': '1000px'},
                        id='table2',
                        #active_cell= None
                        ),
    
    html.H2(id='test')

], style={'background-color': 'purple'})



# ------------------------------------------------------------------------------
# Connect Leaflet Map to Dash Components
@cache.memoize()

#api call function
def apiCall(w):
    request = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.streams/items.json'
    query = '?properties=watershed_group_code,segmented_stream_id&filter=watershed_group_code%20=%20%27' + w + '%27' #this query slows things down for some reason

    request1 = 'https://features.hillcrestgeo.ca/bcfishpass/collections/bcfishpass.crossings/items.json'
    query1 = '?properties=aggregated_crossings_id,pscis_status,barrier_status,access_model_ch_co_sk,all_spawningrearing_per_barrier,all_spawningrearing_km&filter=watershed_group_code%20=%20%27' + w + '%27%20AND%20all_spawningrearing_km%3e0'

    response_API = requests.get(request+query)
    response_API1 = requests.get(request1+query1)

    parse = response_API.text
    parse1 = response_API1.text

    return parse, parse1

def get_data(features):
    Passable = []
    potential = []
    barrier = []
    other = []
    for i in range(len(features)):
        if features[i]['properties']['barrier_status'] == 'PASSABLE':
            Passable.append(
                dl.CircleMarker(
                    color='white',
                    fillColor = '#32cd32',
                    fillOpacity = 1, 
                    center = (features[i]['geometry']['coordinates'][1], features[i]['geometry']['coordinates'][0]), 
                    children=[
                        dl.Tooltip(str(features[i]['properties']['aggregated_crossings_id'])),
                        dl.Popup(str(features[i]['properties']['aggregated_crossings_id'])),
                    ],
                )
            )
        elif features[i]['properties']['barrier_status'] == 'POTENTIAL':
            potential.append(
                dl.CircleMarker(
                    color='white',
                    fillColor = '#ffb400',
                    fillOpacity = 1, 
                    center = (features[i]['geometry']['coordinates'][1], features[i]['geometry']['coordinates'][0]), 
                    children=[
                        dl.Tooltip(str(features[i]['properties']['aggregated_crossings_id'])),
                        dl.Popup(str(features[i]['properties']['aggregated_crossings_id'])),
                    ],
                )
            )
        elif features[i]['properties']['barrier_status'] == 'BARRIER':
            barrier.append(
                dl.CircleMarker(
                    color='white',
                    fillColor = '#d52a2a',
                    fillOpacity = 1, 
                    center = (features[i]['geometry']['coordinates'][1], features[i]['geometry']['coordinates'][0]), 
                    children=[
                        dl.Tooltip(str(features[i]['properties']['aggregated_crossings_id'])),
                        dl.Popup(str(features[i]['properties']['aggregated_crossings_id'])),
                    ],
                )
            )
        else:
            other.append(
                dl.CircleMarker(
                    color = 'white',
                    fillColor = '#965ab3',
                    fillOpacity = 1,
                    center = (features[i]['geometry']['coordinates'][1], features[i]['geometry']['coordinates'][0]), 
                    children=[
                        dl.Tooltip(str(features[i]['properties']['aggregated_crossings_id'])),
                        dl.Popup()
                    ],
                )
            )

    pass_cluster = dl.MarkerClusterGroup(id='markers', children=Passable)
    pot_cluster = dl.MarkerClusterGroup(id='markers', children=potential)
    bar_cluster = dl.MarkerClusterGroup(id='markers', children=barrier)
    other_cluster = dl.MarkerClusterGroup(id='markers1', children=other)
    return pass_cluster, pot_cluster, bar_cluster, other_cluster

# features = gjson['features']
def get_tabledata(features):
    id_list = []
    for i in range(len(features)):
        pscis=features[i]['properties']['pscis_status']
        barr=features[i]['properties']['barrier_status']
        acc=features[i]['properties']['access_model_ch_co_sk']
        all=features[i]['properties']['all_spawningrearing_per_barrier']
        cross_id = str(features[i]['properties']['aggregated_crossings_id'])
        lat = features[i]['geometry']['coordinates'][1]
        lon = features[i]['geometry']['coordinates'][0]

        temp = dict(id = cross_id, pscis_status=pscis, barrier_status=barr, access_model_ch_co_sk=acc, all_spawningrearing_per_barrier=all, lat = lat, lon = lon)

        id_list = id_list + [temp,]
    return id_list



@app.callback(
    [Output('pass', 'children'), Output('pot', 'children'), Output('bar', 'children'), Output('other', 'children'), Output('streams', 'data'), Output('table2','data')], [Input('watershed', 'value'), Input('dd', 'value')]
)
def update_map(value, priority):
    
    
    if value == 'BULK':
        parse, parse1 = apiCall('BULK')
        B_gjson = json.loads(parse1)
        B_stream = json.loads(parse)
        features = B_gjson['features']
        return get_data(features)[0], get_data(features)[1], get_data(features)[2], get_data(features)[3], B_stream, get_tabledata(features)
    elif value == 'LNIC':
        parse, parse1 = apiCall('LNIC')
        B_gjson = json.loads(parse1)
        B_stream = json.loads(parse)
        features = B_gjson['features']
        return get_data(features)[0], get_data(features)[1], get_data(features)[2], get_data(features)[3], B_stream, get_tabledata(features)
    elif value == 'ELKR':
        parse, parse1 = apiCall('ELKR')
        B_gjson = json.loads(parse1)
        B_stream = json.loads(parse)
        features = B_gjson['features']
        return get_data(features)[0], get_data(features)[1], get_data(features)[2], get_data(features)[3], B_stream, get_tabledata(features)
    elif value == 'HORS':
        parse, parse1 = apiCall('HORS')
        B_gjson = json.loads(parse1)
        B_stream = json.loads(parse)
        features = B_gjson['features']
        

        if priority == 'intermediate':
            data = []
            for i in range(0, len(inter_table.iloc[:,0])):
                id_list = get_tabledata(features)
                id_index = dict((p['id'],j) for j,p in enumerate(id_list))
                index1 = id_index.get(str(inter_table.iloc[:,0][i]), -1)
                data = data + [id_list[index1],]
            return get_data(features)[0], get_data(features)[1], get_data(features)[2], get_data(features)[3], B_stream, data
        elif priority == 'priority':
            data=[]
            for i in range(0, len(prior_table.iloc[:,0])):
                id_list = get_tabledata(features)
                id_index = dict((p['id'],j) for j,p in enumerate(id_list))
                index1 = id_index.get(str(prior_table.iloc[:,0][i]), -1)
                data = data + [id_list[index1],]
            return get_data(features)[0], get_data(features)[1], get_data(features)[2], get_data(features)[3], B_stream, data
        else:
           return get_data(features)[0], get_data(features)[1], get_data(features)[2], get_data(features)[3], B_stream, get_tabledata(features) 
        
    
    else: 
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
    
@app.callback(
    [Output('map', 'center'), Output('map', 'zoom')], [Input('table2', 'active_cell'), Input('watershed', 'value')]
)
def marker(cell, value):
    if value == 'HORS':
        if cell['column_id'] == "id":
            parse1 = apiCall(value)[1]
            B_gjson = json.loads(parse1)
            features = B_gjson['features']
            id_list = get_tabledata(features)
            for i in id_list:
                if str(i['id']) == cell['row_id']:
                    lat = i['lat']
                    lon = i['lon']
                    center = [lat,lon]
            return center, 16 
    elif value == 'BULK':
        if cell['column_id'] == "id":
            parse1 = apiCall(value)[1]
            B_gjson = json.loads(parse1)
            features = B_gjson['features']
            id_list = get_tabledata(features)
            for i in id_list:
                if str(i['id']) == cell['row_id']:
                    lat = i['lat']
                    lon = i['lon']
                    center = [lat,lon]
            return center, 16

    elif value == 'LNIC':
        if cell['column_id'] == "id":
            parse1 = apiCall(value)[1]
            B_gjson = json.loads(parse1)
            features = B_gjson['features']
            id_list = get_tabledata(features)
            for i in id_list:
                if str(i['id']) == cell['row_id']:
                    lat = i['lat']
                    lon = i['lon']
                    center = [lat,lon]
            return center, 16

    elif value == 'ELKR':
        if cell['column_id'] == "id":
            parse1 = apiCall(value)[1]
            B_gjson = json.loads(parse1)
            features = B_gjson['features']
            id_list = get_tabledata(features)
            for i in id_list:
                if str(i['id']) == cell['row_id']:
                    lat = i['lat']
                    lon = i['lon']
                    center = [lat,lon]
            return center, 16           
    
    else:
        return dash.no_update, dash.no_update
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(mode='inline', port = random.choice(range(2000, 10000)))

