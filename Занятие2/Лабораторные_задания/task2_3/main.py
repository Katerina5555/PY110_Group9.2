from itertools import count

def pow_gen(base: int, step: int = 1):
    for i in count(0, step):
        yield base ** i
    # counter = 0
    # while True:
    #     yield base ** counter
    #     counter += 1

    # TODO записать функцию-генератор


if __name__ == "__main__":
    pow_numbers = pow_gen(10, 1)

    for _ in range(5):
        print(next(pow_numbers))
