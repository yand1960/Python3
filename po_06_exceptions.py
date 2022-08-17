with open("data/numbers.txt") as f:
    text = f.read()

lines = text.split("\n")
# print(lines)
for line in lines:
    try:
        splitted = line.split(";")
        x = int(splitted[0])
        y = int(splitted[1])
        z = x / y
        print(f"{x}:{y}={z}")
    except ZeroDivisionError:
        print(f"{x}:{y}=99999")
    except Exception as e:
        # pass # не глотайте ошибку, это антипаттерн
        print(f"ERROR in line {line}\n\t{e}")
    # finally:
    #     print("The line has been processed")