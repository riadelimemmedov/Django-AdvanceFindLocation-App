from django.contrib.gis.geoip2 import GeoIP2

#Helper Functions
def get_geo(ip):#yeni biz bura ip adres veririk bu ip gore bize location verir
    g = GeoIP2()
    country = g.country(ip)
    city = g.city(ip)
    lat,lon = g.lat_lon(ip)
    return country,city,lat,lon

def get_center_coordinates(latA,longA,latB=None,longB=None):
    cord = (latA,longA)#default budur baslandgic deyer kimi yeni
    
    print('Cord default value', cord)
    if latB:
        cord = [(latA+latB)/2,(longA+longB)/2]
        print('Clicked after value',cord)
    return cord

def get_zoom(distance):
    if(distance<=100):
        return 8
    elif distance>100 and distance<=5000:
        return 4
    else:
        return 2

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
