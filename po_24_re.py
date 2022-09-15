passport = "12 34 567890"

valid = True

if len(passport) != 12:
    valid = False

if passport[2] != " " or passport[5] != " ":
    valid = False

for i in [0, 1, 3, 4, 6, 7, 8, 9, 10, 11]:
    if passport[i] < "0" or passport[i] > "9":
        valid = False

print(valid)