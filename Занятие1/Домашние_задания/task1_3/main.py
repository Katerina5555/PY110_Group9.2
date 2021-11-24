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