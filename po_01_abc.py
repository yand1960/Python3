import datetime as dt

# print("Hello, world!")


def days_left_till_new_year():
    today = dt.date.today()
    new_year = dt.date(today.year + 1, 1, 1)
    return (new_year - today).days

if __name__ == "__main__":
    print(days_left_till_new_year())

    x = 23
    y = 2
    result = x + y
    print(f"{x}+{y}={result}")

    first_name = "Yuri"
    last_name = 'Andrienko'
    # full_name = first_name + " " + last_name
    full_name = f"{first_name} {last_name}"
    print(full_name)

    full_name = "Vasya Pupkin"
    space_position = full_name.find(" ")
    first_name = full_name[0:space_position]
    print(first_name)
    last_name = full_name[space_position + 1:]
    print(last_name)
    name_with_initial = f"{first_name[0]}.{last_name}"
    print(name_with_initial)
    # todo: Pupkin, Vasya
    official_name = f"{last_name}, {first_name}"
    print(official_name)

    numbers = [1, 2, 3, 44, 4, 0, 2, 22]
    numbers.append(77)
    print(numbers[2])

    for x in numbers:
        if x > 10:
            print(x)

    # for i in range(0, len(numbers)):
    #     print(numbers[i])

    data1 = [1, 2, 0, 3]
    data2 = [3, 2, 4, 5]

    # Алгоритм с асимтотикой O(n2)
    for x1 in data1:
        for x2 in data2:
            if x1 == x2:
                print(x1)
