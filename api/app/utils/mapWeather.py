#MODELS 
from ..models.weather import Weather
#UTILS
from ..utils.mapLocation import MapLocation

class MapWeather():
    def mapObjectToWeather(obj):
        print(object)
        weather: Weather = Weather(location=obj['location'], temp_c=obj['current']['temp_c'], temp_f=obj['current']['temp_f'],
         condition=obj['current']['condition'], humidity=obj['current']['humidity'], feelslike_c=obj['current']['feelslike_c'],
          feelslike_f=obj['current']['feelslike_f'], last_updated=obj['current']['last_updated'])
        return weather