#PYDANTIC
from pydantic import BaseModel

#MODELS
from .location import Location

class Weather(BaseModel):
    location: Location
    temp_c: int
    temp_f: int
    condition: str
    humidity: int
    feelslike_c: int
    feelslike_f: int
    last_update: str
