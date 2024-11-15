# from jsonSerializer import JsonSerializer
from xmlSerializer import XmlSerializer
from storage import Storage
from movie import Comedy
from movieService import MovieService

def main():
    serializer = XmlSerializer()
    storage = Storage(serializer)
    service = MovieService(storage)

    while True:
        print("\nВыберите действие:")
        print("1. Добавить фильм")
        print("2. Обновить фильм")
        print("3. Удалить фильм")
        print("4. Показать все фильмы")
        print("5. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            movie_type = input("Введите тип фильма: ")
            name = input("Введите название фильма: ")
            duration = int(input("Введите длительность фильма (в минутах): "))
            year = int(input("Введите год выпуска: "))
            service.create_movie(movie_type, name, duration, year)

        elif choice == "2":
            movie_type = input("Введите тип фильма: ")
            name = input("Введите название фильма: ")
            duration = int(input("Введите новую длительность фильма (в минутах): "))
            year = int(input("Введите новый год выпуска: "))
            service.update_movie(movie_type, name, duration, year)

        elif choice == "3":
            movie_type = input("Введите тип фильма: ")
            name = input("Введите название фильма: ")
            service.delete_movie(movie_type, name)

        elif choice == "4":
            service.read_movies()

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()


    
    
    
    
    
    
    
    
    

    
    

        

