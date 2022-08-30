# Практический пример так называемого класса данных (класс-сущности)

class Employee:

    def __init__(self, first_name: str, last_name: str, salary: float):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}"

if __name__ == "__main__":
    people: [Employee] = []
    people.append(Employee(first_name="Yuri", last_name="Andrienko", salary=123456))
    people.append(Employee(first_name="Vasya", last_name="Pupkin", salary=77777))
    people.append(Employee(first_name="Masha", last_name="Mashkina", salary=300000))

    for emp in people:
        # print(f"{emp.first_name} {emp.last_name.upper()} has salary {emp.salary} ")
        print(emp)

    print(max(people, key=lambda emp: emp.salary).last_name)
