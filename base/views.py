from django.shortcuts import render
import requests
import json
import math

# Getting API Key
API_KEY = '97eeb5a6719c4c5d945f72163de714ed'

# Create your views here.
def home(request):
    if request.method=='POST':
        city = request.POST['city'][0]
        url = f'https://api.weatherbit.io/v2.0/current?city={city}&key={API_KEY}'
        try:
            json_data = requests.get(url)
            data = json.loads(json_data.content)
            temp = data['data'][0]['temp']
            weather = data['data'][0]['weather']['description']
            code = data['data'][0]['weather']['code']
            humidity = data['data'][0]['rh']
            wind = data['data'][0]['wind_spd']
    
            context = {
                'whole_data':data,
                'temp': temp,
                'humidity': math.trunc(humidity),
                'wind': math.trunc(wind),
                'weather': weather,
                'code':code,
                'city':city.title()
            }
        except:
            no_data = "Make Sure You Entered Correct City"
            context = {
                'no_data':no_data
            }

        return render(request, 'weather.html', context)
    return render(request, 'weather.html', {'no_data':'Please Enter City'})