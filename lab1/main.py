def swap(array:list, index1: int, index2: int):
    array[index1], array[index2] = array[index2], array[index1]

def subarray(array):
    N = len(array)
    if N == 1 or array == sorted(array.copy()):
        return (-1, -1)

    list_for_index = set()
    for i in range(0, N-1):

        min_index = i
        for j in range(i + 1, N):

            if array[j] < array[min_index]:
                min_index = j
                list_for_index.add(i)
                list_for_index.add(j)
                swap(array, i, min_index)

    min_index = min(list_for_index)
    max_index = max(list_for_index)
    return (min_index, max_index)

if __name__ == "__main__":
    array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

    print(subarray(array))
