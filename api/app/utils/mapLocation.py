#MODELS 
from ..models.location import Location

class MapLocation():
    def mapLocation(obj):
        location: Location = Location(obj[0[0]], obj[0[1]], obj[0[2]], obj[0[7]])
        return location