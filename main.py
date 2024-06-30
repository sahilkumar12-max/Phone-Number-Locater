import phonenumbers
from phonenumbers import geocoder
import folium

from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

key = "5181186f40ff4296858b19db6de8ed17"

number  = input("Enter Your umber with Country Code : ")

check_number = phonenumbers.parse(number)
number_location =  geocoder.description_for_number(check_number,"en")
print(check_number)
print(number_location)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

  
geocoder = OpenCageGeocode(key)
query = str(number_location)
results = geocoder.geocode(query)

lat  = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

map_loaction =  folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng],popup=number_location).add_to(map_loaction)
map_loaction.save("mylocation.html")

