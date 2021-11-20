def min_len_check(fn):
    # TODO записать обертку для исходной функции
    def wrapper(arg):

        # TODO написать проверку положительности аргумента arg
        if len(arg) < 10:
            raise ValueError("Строка слишком короткая")
        return fn(arg)
    return wrapper


# TODO задекорировать функцию
@min_len_check
def some_func(str_arg: str):
    print(str_arg)


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо

    some_func("Short str")  # ValueError("Строка слишком короткая")
