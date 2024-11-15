class Movie:
    def __init__(self, name: str, duration: int, year: int):
        self.__name = name
        self.__duration = duration
        self.__year = year
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year
        
    def get_genre(self):
        pass

class Comedy(Movie):
    def get_genre(self):
        return "Жанр - комедия"
    
class Horror(Movie):
    def get_genre(self):
        return "Жанр - ужасы"
    
class Drama(Movie):
    def get_genre(self):
        return "Жанр - драма"
    
class Fantasy(Movie):
    def get_genre(self):
        return "Жанр - фантастика"
    
class Detective(Movie):
    def get_genre(self):
        return "Жанр - детектив"
    
class Melodrama(Movie):
    def get_genre(self):
        return "Жанр - мелодрама"
    
class Documentary(Movie):
    def get_genre(self):
        return "Жанр - документальный"
    
class Cartoons(Movie):
    def get_genre(self):
        return "Жанр - мультики"
    
class Anime(Movie):
    def get_genre(self):
        return "Жанр - аниме"
    
class ActionMovie(Movie):
    def get_genre(self):
        return "Жанр - боевик"

    

    
    
    
    
    
    
    
    
    

    
    

        

