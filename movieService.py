from storage import Storage
from constants import MOVIE_FACTORY_MAP

class MovieService():
    def __init__(self, storage: Storage) -> None:
        self.__storage = storage
        self.__movies = []

    def create_movie(self, movie_type: str, name: str, duration: int, year: int) -> None:
        if movie_type not in MOVIE_FACTORY_MAP:
            raise TypeError
        movie = MOVIE_FACTORY_MAP[movie_type](name, duration, year)
        self.__movies.append(movie)
        self.__storage.save_to_file(self.__movies)
        print("Фильм успешно добавлен.")

    def update_movie(self, name: str, duration: int, year: int) -> None:
        self.__movies = self.__storage.load_from_file()
        for movie in self.__movies:
            if movie.name == name:
                movie.duration = duration
                movie.year = year
                self.__storage.save_to_file(self.__movies)
                print("Фильм успешно обновлен.")
                return
        print("Фильм не найден.")

    def delete_movie(self, name: str) -> None:
        self.__movies = self.__storage.load_from_file()
        for movie in self.__movies:
            if movie.name == name:
                self.__movies.remove(movie)
                self.__storage.save_to_file(self.__movies)
                print("Фильм успешно удален.")
                return
        print("Фильм не найден.")

    def read_movies(self) -> None:
        self.__movies = self.__storage.load_from_file()
        if not self.__movies:
            print("База фильмов пуста.")
            return
        for movie in self.__movies:
            print(f"Название: { movie.name }, Длительность: { movie.duration }, Год: { movie.year }, Тип: { movie.__class__.__name__ }")
