#Python
from os import environ
from typing import List
import requests
import json
#Fastapi
from fastapi import APIRouter, HTTPException

from app.utils.mapNews import MapNews

#Models
from ..models.news import News

NEWS_APY_KEY = environ['news_api_key']

router = APIRouter()

@router.get(
    path='/news/{city}',
    summary='Get the news for an specific city',
    response_model=List[News],
    tags=['news']
)
def get_city_news(city: str):
    """
    Get most relevant news from a city

    This Path Operation get a list of 10 most popular news related to a city

    - Path Parameters:
        - **city: str** -> This parameter requires the city´s name in English as a string

    Returns a list with the result of the news
    """
    key_header = {"x-api-key": NEWS_APY_KEY}
    news_responde_raw = requests.get(f'https://api.newscatcherapi.com/v2/search?q={city}&page_size=12', headers=key_header)
    if news_responde_raw.status_code == 404 or news_responde_raw.status_code == 400:
        raise HTTPException(status_code=404, detail="Not news were found")
    news_responde_raw = json.loads(news_responde_raw.content.decode('utf-8'))['articles']   
    news_response: News = MapNews.mapObjectToNews(news_responde_raw)
    return news_response