# распарсит инпут и вывести только цитаты по отдельности
import codecs
#-*- coding: utf8 -*-
import re
def task():
    with open("input.txt", "r", encoding='utf-8'):
        pattern = re.findall(r'"""(.|\n)+?"""', "input.txt")
        print(pattern)

# pattern = """(.|\n)+?"""

if __name__ == "__main__":
    task()
    with open("input.txt") as file:
        for line in file:
            print(line, end="")
    pass
