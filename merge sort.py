def merge_list(a, b):
    """функция слияния двух отсортированных списков"""
    c = []
    N = len(a)
    M = len(b)

    i = 0
    j = 0
    while i < N and j < M:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    return c


def split_and_merge_list(a):
    """функция деления списка и слияния списков в общий отсортированный список"""
    N1 = len(a) // 2
    part1 = a[:N1]     # деление массива на два примерно равной длины
    part2 = a[N1:]

    if len(part1) > 1: # если длина 1-го списка больше 1, то делим дальше
        part1 = split_and_merge_list(part1)
    if len(part2) > 1: # если длина 2-го списка больше 1, то делим дальше
        part2 = split_and_merge_list(part2)

    return merge_list(part1, part2)   # слияние двух отсортированных списков в один


if __name__ == '__main__':
    array = [int(_) for _ in input().split(' ')]
    result = split_and_merge_list(array)
    print(result)
