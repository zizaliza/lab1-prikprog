import json
from serializer import Serializer

class JsonSerializer(Serializer):
    def to_format(self, movies: dict) -> str:
        movies_data = [{"type": movie.__class__.__name__, "name": movie.name, "duration": movie.duration} for movie in movies]
        return json.dumps(movies_data, indent=4)
    
    def from_format(self, data: dict) -> any:
       return json.loads(data)

    