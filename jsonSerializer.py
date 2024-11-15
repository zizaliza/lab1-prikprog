import json
from serializer import Serializer

class JsonSerializer(Serializer):
    def to_format(self, movies: dict) -> str:
        return json.dumps(movies, indent=4)
    
    def from_format(self, data: dict) -> any:
       return json.loads(data)

    