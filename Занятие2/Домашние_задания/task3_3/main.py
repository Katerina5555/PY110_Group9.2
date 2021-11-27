def output_type_list(fn):
    def wrapper(*args, **kwargs):

        fn(*args, **kwargs)
        for index, arg in enumerate(args):
            print(f"Позиционный аргумент {index}: {arg}")
            if arg is not iter:
                raise TypeError(f"Объект {index} {arg} не является итерируемым")
            else:
                continue
        for key, kwarg in kwargs.items():
            print(f"Именованный аргумент {key}: {kwarg}")
            if kwarg is not iter:
                raise TypeError(f"Объект {key} {kwarg} не является итерируемым")
            else:
                continue
    return wrapper

@output_type_list
def return_list():
    return []


if __name__ == "__main__":
    return_list()

