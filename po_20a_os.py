# скопировать в folder3 те файлы из folder1, которых нет в folder2
# Инкапсуляция функцией

import os
import shutil


def copy_unique_files(folder1, folder2, folder3):

    files1 = os.listdir(folder1)
    files2 = os.listdir(folder2)

    unique_files = list(set(files1).difference(set(files2)))

    for file in unique_files:
        shutil.copy(f"{folder1}/{file}", f"{folder3}/{file}")


if __name__ == "__main__":
    copy_unique_files("data/folder1", "data/folder2", "data/folder3")
