from django.shortcuts import render
import folium
def index(request):
    m = folium.Map(location)
    m = m._repr_html_()
    context = {
        "m": m
    }
    return render(request, "index.html",  context)

