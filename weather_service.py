import requests
import os
from redis_client import redis_client

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5"

async def get_weather(city: str):
    cache_key = f"weather:{city}"
    cached_weather = redis_client.get(cache_key)
    
    if cached_weather:
        return cached_weather
    
    url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    weather_data = response.json()
    
    redis_client.set(cache_key, weather_data, ex=300)  # Cache for 5 minutes
    
    return weather_data

async def get_forecast(city: str):
    cache_key = f"forecast:{city}"
    cached_forecast = redis_client.get(cache_key)
    
    if cached_forecast:
        return cached_forecast
    
    url = f"{BASE_URL}/forecast?q={city}&appid={API_KEY}"
    response = requests.get(url)
    forecast_data = response.json()
    
    redis_client.set(cache_key, forecast_data, ex=600)  # Cache for 10 minutes
    
    return forecast_data
