from itertools import count


def task():
    counter = count(100, 10)

    # TODO распечатать с столбик первые 10 чисел бесконечного итератора
    for _ in range(10):  # TODO напечатать первые 10 чисел
        print(next(counter))

if __name__ == "__main__":
    task()
