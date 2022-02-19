import time
import numpy as np


def get_smallest_unmarked(arr: list, marked: list):
    smallest_index = None

    # get index of first unmarked element
    for i, mark in enumerate(marked):
        if not mark:
            smallest_index = i
            break

    # if any element after that is smaller, return it instead
    for index in range(smallest_index + 1, len(arr)):
        if not marked[index] and arr[index] < arr[smallest_index]:
            smallest_index = index

    return smallest_index

def selection_sort(arr: list):
    """Sorts an array in ascending order

    Args:
        arr (list): array to sort

    Return:
        sorted_arr (list): sorted array
    """
    sorted_arr = []

    marked = [False for i in range(len(arr))]

    for x in range(len(marked)):
        smallest_index = get_smallest_unmarked(arr, marked)
        sorted_arr.append(arr[smallest_index])
        marked[smallest_index] = True

    return sorted_arr

if __name__ == "__main__":
    sorted_arr  = selection_sort([1, -1, 4, 5, 0, 10, 7, 6, 5, 1, 8, 99])
    print(sorted_arr)

    start_time = time.time()
    sorted_arr  = selection_sort(np.random.randint(1,1000,500))
    end_time = time.time()
    print("Sorting took {:e} seconds".format(end_time - start_time))
    print(sorted_arr)

