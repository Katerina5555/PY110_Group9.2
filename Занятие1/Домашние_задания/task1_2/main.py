# Напишите программу Python, которая преобразует все символы в верхний и нижний
# регистры и удаляет повторяющиеся буквы из заданной последовательности.
# Используйте функцию map ().

# def list_map(words: list) -> list:
#     return list(map(str.capitalize, words))
#
# def list_map_2(words: list) -> list:
#     return list(map(str.lower, words))
#
# def task():
#     list_words = ['U', 'f', 'a', 'b', 'i', 'o', 'E']
#     list_cap = list_map(list_words)
#     list_low = list_map_2(list_words)
#
#     for letter_1, letter_2 in zip(list_cap, list_low):
#         print(list((letter_1 + letter_2)))
#
if __name__ == "__main__":
    # task()
    list_words = ['U', 'f', 'a', 'b', 'i', 'o', 'E']
    print(set(map(lambda x: (x.upper(), x.lower()), set(list_words))))