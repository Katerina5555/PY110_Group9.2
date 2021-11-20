# Напишите программу Python, которая преобразует все символы в верхний и нижний
# регистры и удаляет повторяющиеся буквы из заданной последовательности.
# Используйте функцию map ().

# def list_map(words: list) -> list:
#     return list(map(str.capitalize, words))
#
# def list_map_2(words: list) -> list:
#     return list(map(str.lower, words))
#
# def task():
#     list_words = {'U', 'f', 'a', 'b', 'i', 'o', 'E'}
#     list_cap = list_map(list_words)
#     list_low = list_map_2(list_words)
#
#     for letter_1, letter_2 in zip(list_cap, list_low):
#
#         print(list(letter_1 + letter_2))
#
# if __name__ == "__main__":
#     task()

# Задание 3.
# Напишите скрипт для преобразования заданного списка кортежей в список строк с помощью функции map().
#
# Пример:
# Original list of tuples:
# [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
#
# Convert the said list of tuples to a list of strings:
# ['red pink', 'white black', 'orange green']
#
# Original list of tuples:
# [('Sheridan', 'Gentry'), ('Laila', 'Mckee'), ('Ahsan', 'Rivas'), ('Conna', 'Gonzalez')]
#
# Convert the said list of tuples to a list of strings:
# ['Sheridan Gentry', 'Laila Mckee', 'Ahsan Rivas', 'Conna Gonzalez']

def sum_(word: tuple) -> int:
    return word[0] + " " + word[1]


def task(list_tuples: list) -> list:
    return list(map(sum_, list_tuples))


if __name__ == "__main__":
    line_ = [('Sheridan', 'Gentry'), ('Laila', 'Mckee'), ('Ahsan', 'Rivas'), ('Conna', 'Gonzalez')]

    print(task(line_))