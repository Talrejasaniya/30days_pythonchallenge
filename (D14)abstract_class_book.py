# Import abstract base classes support
from abc import ABCMeta, abstractmethod

# Abstract base class: Book
class Book(object, metaclass=ABCMeta):
    # Constructor to initialize title and author
    def __init__(self, title, author):
        self.title = title
        self.author = author   
    
    # Abstract method that must be implemented in the subclass
    @abstractmethod
    def display(): 
        pass

# Subclass of Book that implements the abstract method
class MyBook(Book):
    # Constructor to initialize title, author, and price
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price
    
    # Overriding the abstract display method
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

# Taking input from user
title = input()
author = input()
price = int(input())

# Creating an instance of MyBook and displaying its details
new_novel = MyBook(title, author, price)
new_novel.display()
