from xml.etree.ElementTree import Element, SubElement, tostring, fromstring
from xml.dom.minidom import parseString

class XmlSerializer:  # Убрал наследование от несуществующего Serializer
    def to_format(self, movies: list) -> str:  # movies теперь список объектов
        root = Element("Movies")
        for movie in movies:  # Итерируемся по списку объектов
            movie_element = Element(movie.__class__.__name__)
            name_element = SubElement(movie_element, "name")
            name_element.text = movie.name
            duration_element = SubElement(movie_element, "duration")
            duration_element.text = str(movie.duration)
            year_element = SubElement(movie_element, "year")
            year_element.text = str(movie.year)
            root.append(movie_element)
        raw_xml = tostring(root, encoding='unicode')

        dom = parseString(raw_xml)
        pretty_xml = dom.toprettyxml(indent="    ")
        return pretty_xml

    def from_format(self, xml_data: str) -> list:  # xml_data теперь строка XML
        root = fromstring(xml_data)
        movies = []
        for movie_element in root:
            movie_type = movie_element.tag
            name = movie_element.find('name').text
            duration = int(movie_element.find('duration').text)
            year = int(movie_element.find('year').text) # Добавил обработку года
            # Здесь нужно создать объект Movie, а не список.  Предполагается, что у вас есть класс Movie
            movie = Movie(name, duration, year) #  Замените Movie на ваш реальный класс
            movies.append(movie)
        return movies

    def get_format(self) -> str:
        return 'xml'