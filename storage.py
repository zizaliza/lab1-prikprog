from constants import MOVIE_FACTORY_MAP
from serializer import Serializer

class Storage:
    def __init__(self, serializer: Serializer, file_path: str):
        self.__serializer = serializer
        self.__file_path = f'{file_path}.{serializer.get_format()}'

    @property
    def file_path(self) -> str:
        return self.__file_path

    def save_to_file(self, data: dict) -> None:
        serialized_data = self.__serializer.to_format(data)
        with open(self.__file_path, "w", encoding="utf-8") as file:
            file.write(serialized_data)
        print(f"Данные успешно сохранены в файл: {self.__file_path}")

    def load_from_file(self) -> dict:
        with open(self.__file_path, "r", encoding="utf-8") as file:
            serialized_data = file.read()
        data = self.__serializer.from_format(serialized_data)

        movies = []

        for movie in data:
            if movie['type'] not in MOVIE_FACTORY_MAP:
                raise TypeError
            movie = MOVIE_FACTORY_MAP[movie['type']](movie['name'], movie['duration'], movie['year'])
            movies.append(movie)

        print(f"Данные успешно загружены из файла: {self.__file_path}")
        return movies
s