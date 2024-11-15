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
        self.movies = self.__storage.load_from_file("./db.xml")
        for movie in self.__movies:
            if movie.name == name and movie.__class.name.lower() == movie_type.lower():
                movie.duration = duration
                movie.year = year
                self.storage.save_to_file(self.__movies, "./db.xml")
                print("Фильм успешно обновлен.")
                return
        print("Фильм не найден.")

    def delete_movie(self, movie_type: str, name: str):
        self.__movies = self.__storage.load_from_file("./db.xml")
        for movie in self.__movies:
            if movie.name == name and movie.__class.name.lower() == movie_type.lower():
                self.movies.remove(movie)
                self.__storage.save_to_file(self.__movies, "./db.xml")
                print("Фильм успешно удален.")
                return
        print("Фильм не найден.")

    def read_movies(self):
        self.__movies = self.__storage.load_from_file("./db.xml")
        if not self.__movies:
            print("База фильмов пуста.")
            return
        for movie in self.__movies:
            print(f"Название: {movie.name}, Длительность: {movie.duration}, Год: {movie.year}, Тип: {movie.__class.name}")

