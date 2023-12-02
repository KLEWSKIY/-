import time

class Artwork:
    def __init__(self, title, year, author, genre):
        self.title = title
        self.year = year
        self.author = author
        self.genre = genre

    def create(self):

        pass

    def input_info(self):

        pass

    def display_info(self):

        pass

class Technique:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def create(self):

        pass

    def input_info(self):

        pass

    def display_info(self):

        pass

class Painting(Artwork, Technique):
    def __init__(self, title, year, author, genre, width, height, cost, technique_name, material):
        Artwork.__init__(self, title, year, author, genre)
        Technique.__init__(self, technique_name, material)
        self.width = width
        self.height = height
        self.cost = cost

    def create(self):

        pass

    def input_info(self):

        pass

    def display_info(self):

        pass

    def read_cost(self):

        pass

    def change_cost(self, new_cost):

        pass

class Buyer:
    def __init__(self, name):
        self.name = name
        self.offer = 0

    def make_offer(self, offer):
        self.offer = offer

def auction(artworks, buyers, auction_duration):
    start_time = time.time()

    while time.time() - start_time < auction_duration:
        for artwork in artworks:
            offer = float(input(f"Покупець {artwork.title} пропонує ціну: "))
            artwork.change_cost(offer)

    winner = max(buyers, key=lambda x: x.offer)
    print(f"Переможець аукціону: {winner.name} з ціною {winner.offer}")


painting1 = Painting("Моя перша картина", 2020, "Художник1", "Абстракція", 100, 80, 5000, "Фарби", "Полотно")
painting2 = Painting("Ранок у лісі", 2022, "Художник2", "Пейзаж", 120, 90, 8000, "Акрилові", "Картон")

buyer1 = Buyer("Покупець1")
buyer2 = Buyer("Покупець2")

artworks_list = [painting1, painting2]
buyers_list = [buyer1, buyer2]

auction_duration = 60  

auction(artworks_list, buyers_list, auction_duration)


