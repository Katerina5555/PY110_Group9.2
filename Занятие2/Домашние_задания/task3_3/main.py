def output_type_list(fn):
    def wrapper(*args, **kwargs):

        fn(*args, **kwargs)
        for index, arg in enumerate(args):
            print(f"Позиционный аргумент {index}: {arg}")
            if arg is not iter:
                raise TypeError(f"Объект {index} {arg} не является итерируемым")

        for key, kwarg in kwargs.items():
            print(f"Именованный аргумент {key}: {kwarg}")
            if kwarg is not iter:
                raise TypeError(f"Объект {key} {kwarg} не является итерируемым")

    return wrapper

@output_type_list
def return_list():
    return [343]


if __name__ == "__main__":
    return_list()

