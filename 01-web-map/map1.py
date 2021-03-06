from asyncio.streams import FlowControlMixin
from threading import local
from unicodedata import name
import folium
import pandas as pd


volcanoes = pd.read_csv("volcanoes.txt");
volcano_locations = volcanoes[["NAME", "LAT", "LON", "ELEV"]]
map1 = folium.Map()
fg = folium.FeatureGroup(name='My Home Map')

html = """
<h3>Volcano Info:</h4>
Name: {0}
<br />
Elevation: {1} m
"""

for name, lat, lon, elev in volcano_locations.values.tolist():
    iframe = folium.IFrame(html=html.format(name, str(elev)), width=200, height=100)
    fg.add_child(folium.Marker(location=(lat, lon), popup=folium.Popup(iframe), icon=folium.Icon(color='red')))


map1.add_child(fg)
map1.save('map1.html')