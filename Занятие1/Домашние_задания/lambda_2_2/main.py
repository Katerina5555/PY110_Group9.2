# Напишите скрипт для сложения двух заданных списков, используя map и lambda.

def task(elem_list_1, elem_list_2):
     return list(map(lambda x, y: x + y, elem_list_1, elem_list_2))


if __name__ == "__main__":
    list_1 = ['Python', '3', '2', '4', '5', 'version']
    list_2 = ['Hi', '8', '3', 'The', '4', 'End']
    print(task(list_1, list_2))