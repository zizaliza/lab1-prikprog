# from jsonSerializer import JsonSerializer
from xmlSerializer import XmlSerializer
from storage import Storage
from movie import Comedy
from movieService import MovieService

if __name__ == "__main__":   
    xmlSerializer = XmlSerializer()
    storage = Storage(xmlSerializer)
    service = MovieService(storage)
    movie1 = service.create_movie("Drama", "Love", 200, 2005)
    
    

    
    
    
    
    
    
    
    
    

    
    

        

