def task():
    filename = "input.txt"
    with open(filename) as f:  # менеджер контекста открывает файл в режиме чтения в текстовом формате "rt"
        # data = f.readline()
        # print(data)
        for line in f:  # файл является итератором, который построчно возвращает свое содержимое
            print(line.strip())        # TODO c помощью метода строки strip очистить строку от непечатыемых символов
            #print(line, end="")


if __name__ == "__main__":
    task()
