# Полиморфизм и утиная типизация

class Cat:

    def voice(self):
        return "Meaow"


class Dog:

    def voice(self):
        return "Hab"


def call(animal):
    print("Come to me")
    print(animal.voice())


cat = Cat()
dog = Dog()

call(dog)
call(cat)
# call(123)