#PYDANTIC
from pydantic import BaseModel

class Location(BaseModel):
    name: str
    region: str
    country: str
    local_time: str
