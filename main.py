from jsonSerializer import JsonSerializer
from xmlSerializer import XmlSerializer
from storage import Storage
from movieService import MovieService

def main():
    try:
        print("С каким форматов работать (1.json, 2.xml):")
        choice = input("Введите номер действия: ")
        
        if choice == "1":
            serializer = JsonSerializer()
        
        elif choice == "2":
            serializer = XmlSerializer()
        
        else:
            print("Неверный выбор, выход из программы.")
            return
        
        storage = Storage(serializer, "./db")
        service = MovieService(storage)
        service.read_movies()

        while True:
            print("\nВыберите действие:")
            print("1. Добавить фильм")
            print("2. Обновить фильм")
            print("3. Удалить фильм")
            print("4. Показать все фильмы")
            print("5. Выход")

            choice = input("Введите номер действия: ")

            try:
                if choice == "1":
                    movie_type = input("Введите тип фильма: ")
                    name = input("Введите название фильма: ")
                    duration = int(input("Введите длительность фильма (в минутах): "))
                    year = int(input("Введите год выпуска: "))
                    service.create_movie(movie_type, name, duration, year)
                
                elif choice == "2":
                    name = input("Введите название фильма, который хотите изменить: ")
                    duration = int(input("Введите новую длительность фильма (в минутах): "))
                    year = int(input("Введите новый год выпуска: "))
                    service.update_movie(name, duration, year)
                
                elif choice == "3":
                    name = input("Введите название фильма: ")
                    service.delete_movie(name)
                
                elif choice == "4":
                    service.read_movies()
                
                elif choice == "5":
                    print("Выход из программы.")
                    break
                
                else:
                    print("Неверный выбор, попробуйте снова.")
            
            except TypeError:
                print("Ошибка: Неизвестный жанр фильма.")
            except Exception as e:
                print(f"Произошла непредвиденная ошибка: {e}")
    
    except KeyboardInterrupt:
        print("\nПрограмма была прервана пользователем.")
    # except Exception as e:
        # print(f"Произошла ошибка при запуске программы: {e}")

if __name__ == "__main__":
    main()

    
    
    
    
    
    
    
    
    

    
    

        

