#PYDANTIC
from pydantic import BaseModel

#MODELS
from .location import Location

class Condition(BaseModel):
    text: str
    icon: str
    code: int

class Weather(BaseModel):
    location: Location
    temp_c: int
    temp_f: int
    condition: Condition
    humidity: int
    feelslike_c: int
    feelslike_f: int
    last_updated: str
