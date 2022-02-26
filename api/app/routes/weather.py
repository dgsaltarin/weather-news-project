#PYTHON
import requests
import json
#FASTAPI
from fastapi import APIRouter

from app.models.location import Location

#MODELS
from ..models.weather import Weather

#Utils 
from ..utils.mapLocation import MapLocation


router = APIRouter()

@router.get(
    path='/weather/{city}',
    summary='Get the weather for an specific city',
    tags=['weather']
)
def get_city_weather(city: str):
    weather_responde = requests.get('http://api.weatherapi.com/v1/current.json?key=c95e0841860d4390be8153737222502&q=London')
    return json.loads(weather_responde.content.decode('utf-8')) 