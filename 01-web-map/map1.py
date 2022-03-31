from asyncio.streams import FlowControlMixin
from threading import local
from unicodedata import name
import folium
from numpy import argsort

locations = [
    {
        "coordinates": (22.9, 87.75),
        "popup_text": "This. is Marker 1"
    },
    {
        "coordinates": (25.1, 93.8),
        "popup_text": "This is Marker 2"
    }
]

map1 = folium.Map(location=locations[0]["coordinates"], tiles='cartodb positron')
fg = folium.FeatureGroup(name='My Home Map')

for loc in locations:
    fg.add_child(folium.Marker(location=loc["coordinates"], popup=loc["popup_text"], icon=folium.Icon(color='green', icon='home')))

map1.add_child(fg)

map1.save('map1.html')