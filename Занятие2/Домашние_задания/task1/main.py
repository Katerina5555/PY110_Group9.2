def task(number: list) -> int:
    gen_exp = (5 * 4 ** i for i in number)
    return list(gen_exp)


if __name__ == "__main__":
    pow_ = [i for i in range(1, 11)]
    print(task(pow_))