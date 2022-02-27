#PYTHON
import requests
import json
from os import environ
#FASTAPI
from fastapi import APIRouter, HTTPException

from ..database.mongo import collection

#MODELS
from ..models.weather import Weather
from app.models.location import Location

#Utils 
from ..utils.mapWeather import MapWeather

#DATABASE
collection = collection()

WEATHER_APY_KEY = environ['weather_api_key'] or 'c95e0841860d4390be8153737222502'

router = APIRouter()

@router.get(
    path='/weather/{city}',
    summary='Get the weather for an specific city',
    response_model=Weather,
    tags=['weather']
)
def get_city_weather(city: str):
    """
    get the weather of a city

    This Path Operation get the weather from a city providing just the name

    - Path Parameters:
        - **city: str** -> This parameter requires the city´s name as a string

    Returns a weather object with the most relevant weather information of the required city
    """
    weather_responde_raw = requests.get(f'http://api.weatherapi.com/v1/current.json?key={WEATHER_APY_KEY}&q={city}')
    if weather_responde_raw.status_code == 400 or 404:
        raise HTTPException(status_code=404, detail="Location not found")
    weather_responde_raw = json.loads(weather_responde_raw.content.decode('utf-8'))    
    weather_response: Weather = MapWeather.mapObjectToWeather(weather_responde_raw)
    collection.insert_one(weather_response.dict())
    return weather_response