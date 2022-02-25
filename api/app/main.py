#FASTPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#ROUTES
from .routes import news, weather