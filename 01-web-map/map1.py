from asyncio.streams import FlowControlMixin
from threading import local
from unicodedata import name
import folium
import pandas as pd


volcanoes = pd.read_csv("volcanoes.txt");

volcano_locations = volcanoes[["LAT", "LON", "ELEV"]]

map1 = folium.Map()
fg = folium.FeatureGroup(name='My Home Map')


for lat, lon, elev in volcano_locations.values.tolist():
    # print(, vol2)
    fg.add_child(folium.Marker(location=(lat, lon), popup=elev, icon=folium.Icon(color='red')))


map1.add_child(fg)
map1.save('map1.html')