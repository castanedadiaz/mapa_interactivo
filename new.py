import folium

mapa = folium.Map(location=[-34.55758805305217, -58.45165117097104], zoom_start=15)  # Coordenadas de Nueva York

# Añadir un marcador
folium.Marker(
    location=[-34.557835455147405, -58.461650446030816],
     popup='<a href="https://www.cristalpalace.com" target="_blank">¿ Cómo llego al hotel ?</a>',  # Enlace en el popup
     icon=folium.CustomIcon(icon_image="img/Hotel_Icon.png", icon_size=(150, 150))  # URL del ícono
).add_to(mapa)

# Guardar el mapa en un archivo HTML
mapa.save("mapa_nueva_york.html")

print("Mapa guardado como mapa_nueva_york.html")
