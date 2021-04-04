#1
class Book:
    def __init__(self, name, author, date, pages):
        self.name = name
        self.author = author
        self.date = date
        self.pages = pages
    def info(self):
        print(f"name - {self.name}, author - {self.author}, date - {self.date}, pages - {self.pages}")

if __name__ == '__main__':
  book_name = Book ("მგლის ბილიკი", "ალექსანდრე იასაღაშვილი", 1999, 254)
  Book.info(book_name)

#2

a = [24, 234, 654, 33, 27]

class Main(list):
    def __init__(self,list_1):
        self.list_1 = list_1
    def min(self):
        return min(self.list_1)
    def max(self):
        return max(self.list_1)

l = Main(a)
print(f"min value - {l.min()}, max value - {l.max()}")


#3

class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def info(self):
        return f"Name - {self._name}, Age - {self._age}"


class Dog(Animal):
    def __init__(self, breed, color):
        super().__init__(name, age)
        self._name = name
        self._age = age
        self._breed = breed
        self._color = color

    def full_info(self):
        return f"Breed - {self._breed}, Color - {self._color}"


name = "beni"
age = "2 weli"
breed = "haski"
color = "tetri"
a = Animal(name, age)
d = Dog(breed, color)
print(d.info() + ", " + d.full_info())









#4
class CallMixin:
    class Person:
        def __init__(self, name, lname, phone ):
            self.name = name
            self.lmane = lname
            self.phone = phone
        def info (self):
            return f"name -  {self.name}, lastname - {self.lmane}, phone number- {self.phone}"





















