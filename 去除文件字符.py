import os, shutil

# 需要替换的字符
char = '_'


listdir = [_ for _ in os.listdir('.') if not _.startswith('.')]

for file in listdir:
    if char in file:
        shutil.move(file, file.replace(char, ''))
        print("{} to ->>> {}".format(file, file.replace(char, '')))

