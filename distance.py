# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 19:03:03 2022

@author: Rui
"""

import math

def distance(lat1, lon1, lat2, lon2):
    # convert degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # calculate the difference between the latitudes and longitudes
    lat_diff = lat2 - lat1
    lon_diff = lon2 - lon1

    # use the Haversine formula to calculate the distance
    a = (math.sin(lat_diff / 2)**2) + (math.cos(lat1) * math.cos(lat2) * (math.sin(lon_diff / 2)**2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # the radius of the Earth in kilometers
    R = 6371

    # calculate the distance
    distance = R * c

    return distance

# example: calculate the distance between New York and Los Angeles
ny_lat = 40.7128
ny_lon = -74.0060
la_lat = 34.0522
la_lon = -118.2437

distance = distance(ny_lat, ny_lon, la_lat, la_lon)

print(f'The distance between New York and Los Angeles is {distance:.2f} kilometers.')