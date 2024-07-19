from django.shortcuts import render
import requests
from .forms import MainForm
import json

#libs for openmeteo
import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

def index(request):
    if request.method == 'POST':
        key = 'pk.620519c54da1cef96130e4ef25f342da'
        city_name = request.POST.get('city')
        r = requests.get(f'https://us1.locationiq.com/v1/search?key={key}&q={city_name}&format=json&')
        data = json.loads(r.text)
        lat = data[0]['lat']
        lon = data[0]['lon']
        forecast = get_weather(lat, lon)
        date = forecast['date'][0]
        return render (request,
                       'forecast.html',
                       {'forecast': forecast,
                        'city': city_name,
                        'date': date})
    main_form = MainForm()    
    return render(request,
                  'index.html',
                  {'main_form': main_form})

def get_weather(lat, lon):
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "forecast_days": 1
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]

    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

    hourly_data = {"date": pd.date_range(
        start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
        end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = hourly.Interval()),
        inclusive = "left"
    )}
    hourly_data["temperature_2m"] = hourly_temperature_2m

    hourly_dataframe = pd.DataFrame(data = hourly_data)
    return hourly_dataframe