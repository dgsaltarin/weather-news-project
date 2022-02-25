#FASTAPI
from fastapi import APIRouter


router = APIRouter()

@router.get(
    path='/news/{city}',
    summary='Get the news for an specific city',
    tags=['news']
)
def get_city_news(city: str):
    pass