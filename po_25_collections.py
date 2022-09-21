from collections import deque, namedtuple

nums = deque([1, 2, 3])
nums.append(777)
nums.appendleft(-777)
print(nums)

Employee = namedtuple("Employee", ["firstName", "lastName"])

emp1 = Employee(firstName="Yuri", lastName="Andrienko")
print(f"{emp1.lastName}, {emp1.firstName}")