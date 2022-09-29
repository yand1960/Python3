# word1 = "пост"
# word2 = "стоп"

def hash(word):
    return str.join("", sorted(word))

# print(hash(word1), hash(word2))

with open("data/RusDictionary.txt", encoding="utf-8") as f:
    text = f.read()
words = text.split("\n")
# print(words[0:100])

# Наивный алгоритм 0(n2)
# for w1 in words:
#     for w2 in words:
#         if w1 != w2 and  hash(w1) == hash(w2):
#             print(w1, w2)

hash_words = {}
for w in words:
    hash_words[hash(w)] = []

for w in words:
    hash_words[hash(w)].append(w)

for anagrams in hash_words.values():
    if len(anagrams) > 1:
        print(anagrams)

# 1. Найти самое длинное семейство анаграмм
# 2. Желательно одной строкой кода (11:07)
print("Самое длинное семейство анаграмм:")
print(sorted(hash_words.values(), key=len, reverse=True)[0])



