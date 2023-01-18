import folium

m = folium.Map(location=[60.18023577639618, 24.935596245312343], zoom_start=12)
#Supercell Block

folium.Marker([60.16103008178952, 24.921588879761245],
              popup="<h1> SuperCell</h1><img src='download.png' width=400px><p>Fast Growing Startup in Finland </p>",
              tooltip="SUPERCELL",
              icon=folium.Icon(icon='heart',icon_color='red', color='white')).add_to(m)
#WOLT OY Block

folium.Marker([60.17107046850945, 24.934396840473536],
              popup="<h1> Wolt</h1><img src='wolt.png' width=400px><p>Food Delivery Startup in Finland </p>",
              tooltip="Wolt",
              icon=folium.Icon(icon='heart',icon_color='red', color='blue')).add_to(m)

folium.Circle(
    location=(60.167475763399366, 24.930193359684512 ), radius= 900, popup='Promising Startups in Helsinki', color= 'red',
    fill= True,
    fill_color='yellow'
).add_to(m)
m.save("map.html")