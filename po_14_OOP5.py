# Наследование
from nacl.exceptions import ValueError

from po_12_OOP3 import Employee


class Boss(Employee):

    # расширение класса-предка
    def scream(self):
        return f"Я {self.first_name} {self.last_name}! Всем работать!!!"

    # перекрытие метода предка
    def __str__(self):
        return f"Boss: {self.first_name} {self.last_name}"


boss1 = Boss("Bill", "Gates", 12345678)
print(boss1)
print(boss1.scream())


class Manager(Employee):

    def __init__(self, first_name, last_name, salary, level):
        self.level = level
        super().__init__(first_name, last_name, salary)

    def __str__(self):
        return super().__str__().replace("Employee", f"Manager of level {self.level}")

    def __eq__(self, other):
        result = self.first_name== other.first_name
        result = result and self.last_name == other.last_name
        result = result and abs(self.salary - other.salary) < 0.0000001
        result = result and self.level == other.level
        return result

manager1 = Manager("Sam", "Samych", 1234567, 80)
print(manager1)


# класс вроде списка, который принмает только нечетные числа
class ListOfUneven(list):

    def append(self, x):
        if x % 2 == 1:
            super().append(x)
        else:
            raise ValueError("Допустимы только нечетные числа")

    def __setitem__(self, key, value):
        if value % 2 == 1:
            super().__setitem__(key, value)
        else:
            raise ValueError("Допустимы только нечетные числа")

list1 = ListOfUneven()
list1.append(1)
list1.append(3)
print(list1)
try:
    list1.append(2) #error
except Exception as e:
    print(e)
    print("Извините, погорячился!")

# list1[0] = 2 #error
print(list1)

manager1 = Manager("Sam", "Samych", 1234567, 80)
manager2 = Manager("Sam", "Samych", 1234567, 80)

print(manager1 is manager2, manager1 == manager2 )

