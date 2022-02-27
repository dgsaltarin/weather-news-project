#PYDANTIC
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl

class News(BaseModel):
    title: str
    author: Optional[str]
    summary: str
    link: HttpUrl
    media: HttpUrl
