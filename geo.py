# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 19:14:07 2022

@author: Rui
"""

import pandas as pd
df = pd.DataFrame({'name': ['viseu', 'coimbra', 'leiria', 'tomar', 'santarém','aveiro','soure','odemira', 'lagoa', 'faro']})

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geo_IPT")

from geopy.extra.rate_limiter import RateLimiter
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
df['location'] = df['name'].apply(geocode)

df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)

import plotly.express as px
import geopandas as gpd
import shapely.geometry
import numpy as np
import wget

# download a zipped shapefile
wget.download("https://plotly.github.io/datasets/ne_50m_rivers_lake_centerlines.zip")

# open a zipped shapefile with the zip:// pseudo-protocol
geo_df = gpd.read_file("zip://ne_50m_rivers_lake_centerlines.zip")

lats = df['point'].str[0]
lons = df['point'].str[1]
names = df['name']

for feature, name in zip(geo_df.geometry, geo_df.name):
    if isinstance(feature, shapely.geometry.linestring.LineString):
        linestrings = [feature]
    elif isinstance(feature, shapely.geometry.multilinestring.MultiLineString):
        linestrings = feature.geoms
    else:
        continue
    for linestring in linestrings:
        x, y = linestring.xy
        lats = np.append(lats, y)
        lons = np.append(lons, x)
        names = np.append(names, [name]*len(y))
        lats = np.append(lats, None)
        lons = np.append(lons, None)
        names = np.append(names, None)

fig = px.line_geo(lat=lats, lon=lons, hover_name=names)
fig.show()