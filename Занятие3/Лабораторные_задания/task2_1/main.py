import json
import pprint


def task() -> str:
    dict_numbers = {x: x**2 for x in range(1, 11)}  # TODO c помощью dict comprehension сформировать словарь
    # return dict_numbers
    return json.dumps(dict_numbers, indent=4)      # TODO сеализовать словарь в JSON строку


if __name__ == "__main__":
    print(task())
    # pprint.pprint(task(), indent=4, width=1)