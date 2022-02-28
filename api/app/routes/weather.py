#PYTHON
import requests
import json
from os import environ
#FASTAPI
from fastapi import APIRouter, HTTPException, Request, Response

from ..database.mongo import collection

#MODELS
from ..models.weather import Weather
from ..models.session import SessionData

#Utils 
from ..utils.mapWeather import MapWeather

#DATABASE
collection = collection()

WEATHER_APY_KEY = environ['weather_api_key']

router = APIRouter()

@router.get(
    path='/weather/{city}',
    summary='Get the weather for an specific city',
    response_model=Weather,
    tags=['weather']
)
def get_city_weather(city: str, request: Request, response: Response):
    """
    get the weather of a city

    This Path Operation get the weather from a city providing just the name

    - Path Parameters:
        - **city: str** -> This parameter requires the city´s name as a string

    Returns a weather object with the most relevant weather information of the required city
    """
    weather_responde_raw = requests.get(f'http://api.weatherapi.com/v1/current.json?key={WEATHER_APY_KEY}&q={city}')
    if weather_responde_raw.status_code == 400 or weather_responde_raw.status_code == 404:
        raise HTTPException(status_code=404, detail="Location not found")
    weather_responde_raw = json.loads(weather_responde_raw.content.decode('utf-8'))    
    weather_response: Weather = MapWeather.mapObjectToWeather(weather_responde_raw)
    search_hisotry = saveSession(host=request.client.host, city=city)
    response.set_cookie(key='search_history', value= search_hisotry)
    return weather_response

def saveSession(host: str, city: str):
    query = {"host": host}
    if collection.count_documents({"$and":[query]}) == 0:
        session: SessionData = SessionData(host=host, city={city})
        collection.insert_one(session.dict())
        return session.city
    else: 
        for session in collection.find({"$and":[query]}):
            cities = session['city']
            cities.append(city)
            cities = list(dict.fromkeys(cities))
            session: SessionData = SessionData(host=host, city=cities)
            collection.update_one(query,{"$set":session.dict()})
            return cities  
           