def swap(array:list, index1: int, index2: int):
    array[index1], array[index2] = array[index2], array[index1]


def subarray(array: list, is_reversed=False):
    N = len(array)

    if array == sorted(array, reverse=is_reversed):
        return (-1, -1)

    compare = lambda a, b: a > b if is_reversed else a < b

    min_index = N - 1
    max_index = 0

    for i, val in enumerate(array):
        for j in range(i + 1, N):
            if compare(array[j], val):
                min_index = min(min_index, i)
                max_index = max(max_index, j)

    return (min_index, max_index)
