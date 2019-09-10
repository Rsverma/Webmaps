import folium
import pandas

def colorGen(elevation):
    if elevation<1200:
        return "green"
    elif elevation<2400:
        return "orange"
    else:
        return "red"


data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
map = folium.Map(location=[38.58,-99.09],zoom_start=6,titles="Mapbox Bright")

fg = folium.FeatureGroup(name="volcanoes")
fg1 = folium.FeatureGroup(name="population")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el)+" m",
    fill_color=colorGen(el), color ="grey", fill_opacity=0.7))

fg1.add_child(folium.GeoJson(data=open("world.json","r", encoding="utf-8-sig").read(),
style_function=lambda x: {"fillColor": "green" if x["properties"]["POP2005"]<10000000
else "orange" if x["properties"]["POP2005"]<30000000 else "red"}))
map.add_child(fg)
map.add_child(fg1)
map.add_child(folium.LayerControl())
map.save("map1.html")
