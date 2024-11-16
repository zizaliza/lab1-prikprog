from xml.etree.ElementTree import Element, SubElement, tostring, fromstring 
from serializer import Serializer 
from xml.dom.minidom import parseString 
 
class XmlSerializer(Serializer): 
    def to_format(self, movies: dict) -> str: 
        root = Element("Movies") 
        for movie in movies: 
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
        pretty_xml = dom.toprettyxml(indent = "     ") 
        return pretty_xml 
 
    def from_format(self, data: dict) -> list: 
        root = fromstring(data) 
        movies = [] 
        for movie_element in root: 
            movie_type = movie_element.tag 
            name = movie_element.find('name').text 
            duration = int(movie_element.find('duration').text) 
            movies.append([movie_type, name, duration]) 
        return movies 
 
    def get_format(self) -> str: 
        return 'xml'