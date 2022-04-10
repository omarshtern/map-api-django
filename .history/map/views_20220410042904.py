from django.shortcuts import render
import folium
import geocoder 


def index(request):
    location = geocoder.osm("UK")
    lat = location.lat
    lng = location.lng
    country = location.country
    m = folium.Map(location=[19, -12], zoom_start=2)
    folium.Marker([5.594, -0.219], tooltip="Click for more", popup="Ghana").add_to(m)
    folium.Marker([lat, lng], tooltip="Click for more", popup="co").add_to(m)
    m = m._repr_html_()
    context = {
        "m": m
    }
    return render(request, "index.html",  context)
