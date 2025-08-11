from django.shortcuts import render
import requests
import datetime

UNSPLASH_ACCESS_KEY = "6NN-ra9ygp46C-q3oyZ7W_md-Zn_fH20EXu5UeVrKQo"
# Create your views here.
def index(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='karachi'
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d0891e9b7fbf7337ce84ebc6f2373023"
    PARAMS={'units':'metric'}

    data=requests.get(url,params=PARAMS).json()
    description=data['weather'][0]['description']
    icon=data['weather'][0]['icon']
    temp=data['main']['temp']
    day=datetime.date.today()

    # Unsplash API for city image
    unsplash_url = f"https://api.unsplash.com/search/photos?query={city}&client_id={UNSPLASH_ACCESS_KEY}&orientation=landscape"
    image_data = requests.get(unsplash_url).json()
    if image_data['results']:
        city_image = image_data['results'][0]['urls']['regular']
    else:
        city_image = ""

    return render(request,'index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city,'city_image':city_image})