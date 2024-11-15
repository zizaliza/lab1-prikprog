from storage import Storage
from constants import MOVIE_FACTORY_MAP

class MovieService():
    def __init__(self, storage: Storage) -> None:
        self.__storage = storage
        self.__movies = []

    def create_movie(self, movie_type: str, name: str, duration: int, year: int):
        if movie_type not in MOVIE_FACTORY_MAP:
            raise TypeError
        movie = MOVIE_FACTORY_MAP[movie_type](name, duration, year)
        self.__movies.append(movie)
        self.__storage.save_to_file(self.__movies,"./db.xml" )
        
    def update_movie(self, movie_type: str, name: str, duration: int, year: int):
        pass

    def delete_movie(self, movie_type: str, name: str, duration: int, year: int):
        pass

    def read_movies(self, movie_type: str, name: str, duration: int, year: int):
        pass

    
