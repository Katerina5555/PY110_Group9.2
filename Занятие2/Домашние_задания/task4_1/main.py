# def pairwise(iterable):
#     for i in range(len(iterable) - 1):
#         yield f'{iterable[i]}{iterable[i+1]}'
#
# def task(pts):
#     for pair in pairwise(pts):
#         print(pair, end=" ")
#         for x in pair:
#             print(x[0] - x[1])

def pairwaise(iterable):
    for i in range(len(iterable) - 1):
        yield f'{iterable[i]}{iterable[i+1]}'


def calculate_1(x1, y1, x2, y2):
    for x1, y1, x2, y2 in pairwaise(pts):
        return (((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (0.5))

if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]
    print(pairwaise(pts))
    calculate_1(float(pts[1]), float(pts[4]), float(pts[7]), float(pts[10]))