s = "Hello, world!"
print(s[1]) # e
print(s[1:5]) #ello
print(s[:5]) #Hello
print(s[6:]) #world!
print(s[-3:]) #ld!
print(s[2:10:2]) #lo o
print(s[::2]) #Hlo ol!
print(s[::-1]) #!dlrow ,olleH

#https://github.com/yand1960/Python3

#Найти все слова, которые заканчиваются на цо
with open("data/RusDictionary.txt", encoding="utf-8") as f:
    text = f.read()
# print(text[0:1000])
words = text.split("\n")
#print(words[0:100])
for w in words:
    if w[-2:] == "цо":
         print(w)

#    Найти все пары слов-палиндромов "зал-лаз" и т.д. Асимтотика лучше, чем О(n2)
# for w1 in words:
#     for w2 in words:
#         if w1 == w2[::-1]:
#             print(w1, w2)

# reversed = []
# for w in words:
#     reversed.append(w[::-1])

reversed = [w[::-1] for w in words]

#print(reversed[0:100])
# for w in words:
#     if w in reversed:
#         print(w, w[::-1])

print(set(words).intersection(set(reversed)))

print(set(words).intersection(set([w[::-1] for w in words])))
print([ (word, word[::-1]) for word in set(words).intersection(set([w[::-1] for w in words]))])

nums = [1, 2, 3, 10, 11, 12]
# Вывести одной строкой список квадратов этих чисел
print([x * x for x in nums])
