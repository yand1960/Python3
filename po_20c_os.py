# скопировать в folder3 те файлы из folder1, которых нет в folder2
# Инкапсуляция типичным классом

import os
import shutil


class FileProcessing:

    def __init__(self):
        pass
        # Здесь может быть код, который задает внутренние состояния класса
        # и/или выполняет некоторые предварительные действия, необходимые
        # для функционирования класса

    def copy_unique_files(self, folder1, folder2, folder3):

        files1 = os.listdir(folder1)
        files2 = os.listdir(folder2)

        unique_files = list(set(files1).difference(set(files2)))

        for file in unique_files:
            shutil.copy(f"{folder1}/{file}", f"{folder3}/{file}")
        

if __name__ == "__main__":
    FileProcessing().copy_unique_files("data/folder1", "data/folder2", "data/folder3")
