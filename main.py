from fastapi import FastAPI, HTTPException
from redis_client import redis_client
from weather_service import get_weather, get_forecast

app = FastAPI()

@app.get("/weather/current/{city}")
async def read_current_weather(city: str):
    try:
        weather = await get_weather(city)
        return weather
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/weather/forecast/{city}")
async def read_weather_forecast(city: str):
    try:
        forecast = await get_forecast(city)
        return forecast
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
