# Задание 2.
# Напишите скрипт для сортировки списка кортежей по второму элементу с помощью Lambda.

def task():
    list_numbers = [(8, 8), (9, 2), (8, 7)]
    return sorted(list_numbers, key=lambda x: x[::-1])


if __name__ == "__main__":
    print(task())