# 1. Полиморфизм и наследование
# 2. Как Питон обходится без абстрактных класcов и интерфейсов

class Animal:

    def __init__(self):
        raise NotImplementedError("Это абстрактный класс")

    def voice(self):
        return ""


class Cat(Animal):

    def __init__(self):
        pass

    def voice(self):
        return "Meaow"


class Dog(Animal):

    def __init__(self):
        pass

    def voice(self):
        return "Hab"


def call(animal: Animal):
    print("Come to me")
    print(animal.voice())


cat = Cat()
dog = Dog()

call(dog)
call(cat)
# call(123)

a1 = Animal()
call(a1)