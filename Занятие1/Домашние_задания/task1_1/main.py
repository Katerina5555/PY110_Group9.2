def task(numbers: list):
    index_list = range(0, len(numbers), 1)
    for index, num in zip(index_list, numbers):
        print(f'{index}: {num}')


if __name__ == "__main__":
    list_numbers = [0, 6, 2, 3, 4, 22, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    task(list_numbers)

    pass
