class Genre:
    def __init__(self, name, characteristics):
        self.name = name
        self.characteristics = characteristics

    @classmethod
    def create_genre(cls):
        name = input("Введіть назву жанру: ")
        characteristics = input("Введіть характерні особливості: ")
        return cls(name, characteristics)

    def display_genre(self):
        print(f"Жанр: {self.name}")
        print(f"Характерні особливості: {self.characteristics}")


class Carrier:
    def __init__(self, carrier_type, color_scheme, storage_duration):
        self.carrier_type = carrier_type
        self.color_scheme = color_scheme
        self.storage_duration = storage_duration

    @classmethod
    def create_carrier(cls):
        carrier_type = input("Введіть тип носія: ")
        color_scheme = input("Введіть кольорову гаму: ")
        storage_duration = input("Введіть тривалість зберігання: ")
        return cls(carrier_type, color_scheme, storage_duration)

    def display_carrier(self):
        print(f"Тип носія: {self.carrier_type}")
        print(f"Кольорова гама: {self.color_scheme}")
        print(f"Тривалість зберігання: {self.storage_duration} днів")


class Film(Genre, Carrier):
    def __init__(self, title, screenplay_author, director, duration, genre, carrier):
        self.title = title
        self.screenplay_author = screenplay_author
        self.director = director
        self.duration = duration
        Genre.__init__(self, genre.name, genre.characteristics)
        Carrier.__init__(self, carrier.carrier_type, carrier.color_scheme, carrier.storage_duration)

    @classmethod
    def create_film(cls):
        title = input("Введіть назву фільму: ")
        screenplay_author = input("Введіть автора сценарію: ")
        director = input("Введіть режисера: ")
        duration = input("Введіть тривалість фільму: ")
        genre = Genre.create_genre()
        carrier = Carrier.create_carrier()
        return cls(title, screenplay_author, director, duration, genre, carrier)

    def display_film_details(self):
        print(f"Назва фільму: {self.title}")
        print(f"Автор сценарію: {self.screenplay_author}")
        print(f"Режисер: {self.director}")
        print(f"Тривалість: {self.duration} хв.")
        self.display_genre()
        self.display_carrier()


class FilmStorage:
    def __init__(self):
        self.films = []

    def add_film(self, film):
        self.films.append(film)

    def display_films_by_attribute(self, attribute):
        for film in self.films:
            if hasattr(film, attribute):
                print(getattr(film, attribute))

storage = FilmStorage()

film1 = Film.create_film()
storage.add_film(film1)

print("Фільми за носіями:")
storage.display_films_by_attribute("carrier_type")

print("Фільми за авторами сценаріїв:")
storage.display_films_by_attribute("screenplay_author")

print("Фільми за режисерами:")
storage.display_films_by_attribute("director")

print("Фільми за часом до вичерпання терміну зберігання:")
storage.display_films_by_attribute("storage_duration")
