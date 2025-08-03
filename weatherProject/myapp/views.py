from django.shortcuts import render
import requests
import datetime

# Create your views here.
def index(request):
    # if 'city' in request.POST:
    #     city=request.POST['city']
    # else:
    #     city='karachi'
    # url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d0891e9b7fbf7337ce84ebc6f2373023"
    # PARAMS={'units':'metric'}
    return render(request,'index.html')