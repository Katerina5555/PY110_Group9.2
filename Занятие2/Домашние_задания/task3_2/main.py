def output_type_int(fn):
    def wrapper(*args):
        result = fn(*args)
        if not isinstance(result, int):
            raise TypeError(f"Результатом выполнения функции {fn} должно быть число")

    return wrapper

@output_type_int
def return_number() -> int:

    return "x"


if __name__ == "__main__":
    return_number()

