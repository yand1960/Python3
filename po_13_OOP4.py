# Создать класс иникапсулирующий следующий функционал:
# 1. Список слов из какого-то файла (лексемизация)
# 2. Статистику по частоте букв
# 3. Статистика по длине слов

class Vocabulary:

    def __init__(self, path: str, encoding: str = "utf-8", separator: str = "\n"):
        with open(path, encoding=encoding) as f:
            self.text = f.read()
        self.words = self.text.split(separator)

    def statistics_letters(self):
        abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        results = {}
        for letter in abc:
            results[letter] = self.text.count(letter)
        return results

    def statistics_length(self):
        results = {}
        for i in range(0, 30):
            results[i] = 0
        for w in self.words:
            results[len(w)] += 1
        return results



vocab1 = Vocabulary("data/RusDictionary.txt")
words1 = vocab1.words
print(words1[0:100])
print(vocab1.statistics_letters())
print(vocab1.statistics_length())

