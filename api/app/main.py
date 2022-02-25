#FASTPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#ROUTES
from .routes import news, weather

app = FastAPI()

#Cors configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'] 
)

#Add weather methods
app.include_router(
    weather.router,
    prefix='/weather',
    tags=['weather']
)

#Add news methods
app.include_router(
    news.router,
    prefix='/news',
    tags=['news']
)