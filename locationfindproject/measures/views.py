
from turtle import color
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,get_object_or_404
from geopy.geocoders import Nominatim
from .utils import *
from geopy.distance import geodesic
import folium
from .forms import *
from .models import *

# Create your views here.

def calculate_distance_view(request):
    distance = None
    destination = None
    
    obj = get_object_or_404(Measurement,id=1)
    form = MeasurementsModelForm(request.POST or None)
    geolocator = Nominatim(user_agent='measurements')
    
    ip_ = get_client_ip(request)
    print('Ip adresimiz',ip_)
    ip = '72.15.210.99'
    country,city,lat,lon = get_geo(ip_)
    
    print(city)
    print(geolocator.geocode(city))

    location = geolocator.geocode(city)
    
    #?Location 
    l_lat = lat#en
    l_lon = lon#uzunlug
    pointA = (l_lat,l_lon)
    
    print('#########################################################################################')
    
    m = folium.Map(width=800,height=500,location=get_center_coordinates(l_lat,l_lon),zoom_start=8)
    folium.Marker([l_lat,l_lon],tooltip='Click here for more',popup=geolocator.geocode(city),
                    icon=folium.Icon(color='purple')).add_to(m)
    
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            
            destination_input_value = form.cleaned_data.get('destination')
            destination = geolocator.geocode(destination_input_value)


            #?Destination
            d_lat = destination.latitude#en
            d_lon = destination.longitude#uzunlug
            
            #?Calculate Distance
            pointB = (d_lat,d_lon)
            
            distance = round(geodesic(pointA,pointB).km,2)
            print('mesafe',distance)
            
            #?Map Destionation
            m = folium.Map(width=800,height=500,location=get_center_coordinates(l_lat,l_lon,d_lat,d_lon),zoom_start=get_zoom(distance))
            
            #*Location
            folium.Marker([l_lat,l_lon],tooltip='Click here for more',popup=geolocator.geocode(city),
                    icon=folium.Icon(color='purple')).add_to(m)
            
            #*Destination
            folium.Marker([d_lat,d_lon],tooltip='Click destionation here',popup=destination,
                        icon=folium.Icon(color='red',icon='cloud')).add_to(m)
            
            #*Draw the line between location and destination
            line = folium.PolyLine(locations=[pointA,pointB],weight=5,color='blue')
            m.add_child(line)
            
            instance.location = location
            instance.distance = distance
            instance.save()
            
    m = m._repr_html_()
    
    context = {
        'distance':distance,
        'form':form,
        'map':m,
        'destination':destination,
    }
    
    return render(request,'measures/main.html',context)
