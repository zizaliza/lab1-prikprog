class Movie:
    def __init__(self, name: str, duration: int, year: int):
        self.name = name
        self.duration = duration
        self.year = year

    def to_dict(self):
        return {
            "name": self.name,
            "duration": self.duration,
            "year": self.year

        }