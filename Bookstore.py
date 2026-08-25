'''
Bookstore
    name
    balance
    stock[products]

    register_sell
Product:
    name
    category
    value
    bar_code
    genre
    releaseYear
    
    add_stock
    sell
    register
        Book
            author
            printLength
            publisher
        FilmDVD
            director
            writers
            stars
        VinylRecord
            artist
            totalLength

*args
*kwargs            
'''
import uuid
from datetime import date

class BookStore:
    def __init__(self, name, initialBalance, stock):
        self.name = name
        self.balance = initialBalance
        self.stock = stock

    def register_product_sell(self, product, amount):
        self.balance += amount*(product.value)
        product.sell(amount)
        print(f"\n\tSOLD: [{amount}] - {product.name} ({product.category})"
              f"\n\tR$ {(amount*(product.value)):.2f}")

    def display(self):
        for i, product in enumerate(self.stock):
            print(f"{i+1}° - ")
            product.display()

class Product:
    def __init__(self, name, category, value, genre, releaseYear, stockAmount):
        bar_code = self.generate_bar_code()
        self.register(name, category, value, bar_code, genre, releaseYear, stockAmount)

    def register(self, name, category, value, bar_code, genre, releaseYear, stockAmount):
        self.name = name
        self.category = category
        self.value = value
        self.bar_code = bar_code
        self.genre = genre
        self.releaseYear = releaseYear
        self.stockAmount = stockAmount

    @staticmethod
    def generate_bar_code():
        return uuid.uuid1()

    def add_stock(self, amount):
        self.stockAmount += amount

    def sell(self, amount):
        self.stockAmount -= amount

    def display(self):
        print(f"\t\t*** NAME: {self.name}\n"
              f"\t\t\t CATEGORY: {self.category}\n"
              f"\t\t\t VALUE: {self.value}\n"
              f"\t\t\t BAR CODE: {self.bar_code}\n"
              f"\t\t\t GENRE: {self.genre}\n"
              f"\t\t\t RELEASE YEAR: {self.releaseYear}\n"
              f"\t\t\t STOCK AMOUNT: {self.stockAmount}\n"
              )

class Book(Product):
    def __init__(self, name, value, genre, releaseYear, stockAmount, author):
        super().__init__(name, "Book", value, genre, releaseYear, stockAmount)
        self.author = author

csLewis4Loves = Book("Os 4 Amores", 25, "Teologia", date(1960, 1, 1), 10, "C.S. Lewis")
csLewis3Loves = Book("Os 3 Amores", 30, "Teologia", date(1961, 2, 2), 9, "C.S. Lewis")
csLewis2Loves = Book("Os 2 Amores", 35, "Teologia", date(1962, 3, 3), 8, "C.S. Lewis")
csLewis1Loves = Book("O 1 Amor", 40, "Teologia", date(1963, 4, 4), 7, "C.S. Lewis")

bookStore = BookStore("The Love BookStore", 0, [csLewis1Loves, csLewis2Loves, csLewis3Loves, csLewis4Loves])

csLewis4Loves.display()
bookStore.display()

bookStore.register_product_sell(csLewis4Loves, 5)

csLewis4Loves.display()
bookStore.display()