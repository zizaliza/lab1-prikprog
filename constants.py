from movie import Comedy, Horror, Drama, Fantasy, Detective, Melodrama, Documentary, Anime, ActionMovie
MOVIE_FACTORY_MAP = {

        'Comedy': lambda name, duration, year: Comedy(name, duration, year),
        'Horror': lambda name, duration, year: Horror(name, duration, year),
        'Drama': lambda name, duration, year: Drama(name, duration, year),
        'Fantasy': lambda name, duration, year: Fantasy(name,duration, year),
        'Detective': lambda name, duration, year: Detective(name, duration, year),
        'Melodrama': lambda name, duration, year: Melodrama(name, duration, year),
        'Documentary': lambda name, duration, year: Documentary(name, duration, year),
        'Anime': lambda name, duration, year: Anime(name, duration, year),
        'ActionMovie': lambda name, duration, year: ActionMovie(name, duration, year)
    }