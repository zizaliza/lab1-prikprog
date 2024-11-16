class Movie:
    def __init__(self, name: str, duration: int, year: int):
        self.__name = name
        self.__duration = duration
        self.__year = year
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int) -> None:
        self.__duration = duration

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int) -> None:
        self.__year = year
        
    def get_genre(self) -> str:
        pass

class Comedy(Movie):
    def get_genre(self) -> str:
        return "Жанр - комедия"
    
class Horror(Movie):
    def get_genre(self) -> str:
        return "Жанр - ужасы"
    
class Drama(Movie):
    def get_genre(self) -> str:
        return "Жанр - драма"
    
class Fantasy(Movie):
    def get_genre(self) -> str:
        return "Жанр - фантастика"
    
class Detective(Movie):
    def get_genre(self) -> str:
        return "Жанр - детектив"
    
class Melodrama(Movie):
    def get_genre(self) -> str:
        return "Жанр - мелодрама"
    
class Documentary(Movie):
    def get_genre(self) -> str:
        return "Жанр - документальный"
    
class Cartoons(Movie):
    def get_genre(self) -> str:
        return "Жанр - мультики"
    
class Anime(Movie):
    def get_genre(self):
        return "Жанр - аниме"
    
class ActionMovie(Movie):
    def get_genre(self) -> str:
        return "Жанр - боевик"