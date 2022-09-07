# скопировать в folder3 те файлы из folder1, которых нет в folder2

import os
import shutil

# ----- Задайте пути к трем папкам ------------
FOLDER1 = "data/folder1"
FOLDER2 = "data/folder2"
FOLDER3 = "data/folder3"
# ------------------------------------------------------

os.system("CHCP 65001")
# command = "di" + "r"
# # os.system(command)

files1 = os.listdir(FOLDER1)
files2 = os.listdir(FOLDER2)
# print(files1)

unique_files = list(set(files1).difference(set(files2)))
# print(unique_files)

for file in unique_files:
    print(file)
    shutil.copy(f"{FOLDER1}/{file}", f"{FOLDER3}/{file}")
