#pydantic 
from typing import List
from pydantic import BaseModel

class SessionData(BaseModel):
    host: str
    city: List[str]

