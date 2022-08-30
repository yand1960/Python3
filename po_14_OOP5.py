# Наследование
from po_12_OOP3 import Employee

class Boss(Employee):

    # расширение класса-предка
    def scream(self):
        return f"Я {self.first_name} {self.last_name}! Всем работать!!!"

    #перекрытие метода предка
    def __str__(self):
        return f"Boss: {self.first_name} {self.last_name}"

boss1 = Boss("Bill", "Gates", 12345678)
print(boss1)
print(boss1.scream())
