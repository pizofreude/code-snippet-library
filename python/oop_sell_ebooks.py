# Python OOP mini project about selling ebook with ISBN number

# Create a class called Ebook with the following attributes: isbn, title, author, and price.
class Ebook:
    def __init__(self, isbn, title, author, price):
        """This code defines a class called Ebook.
        An Ebook object has four attributes: isbn, title, author, and price.
        The sell() method prints a message that the ebook with the specified ISBN is being sold.
        """
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price

    # Create a sell() method
    def sell(self):
        print("Selling ebook with ISBN", self.isbn, "by", self.author)

# Create an instance of the Ebook class
ebook1 = Ebook("786-1-24434-508-0", "The Cyclist's Guide to the Web3 Galaxy", "Hafeez Pizofreude", 12.99)
ebook2 = Ebook("978-1-11235-408-1", "The HAQQ Web3 Guide", "Hafeez Al-Haqq", 10.99)

# Sell the ebooks
ebook1.sell()
ebook2.sell()
