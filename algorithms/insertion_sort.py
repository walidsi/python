from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    """Sorts an array of integers inplace

    Args:
        arr (List[int]): input array of integers

    Returns:
        List[int]: the sorted array
    """

    for index in range(1, len(arr)):
        while index > 0:
            if arr[index] <= arr[index - 1]:
                temp = arr[index - 1]
                arr[index - 1] = arr[index]
                arr[index] = temp
            index -= 1

    return arr


arr2 = insertion_sort([3, 5, 6, 1, 2, 7, 9, 0])

print(arr2)


def insertion_sort2(arr: List[int]) -> List[int]:
    for j in range(1, len(arr)):
        insert(arr, j)

    return arr


def insert(arr: List[int], pos: int) -> List[int]:
    """insert array element at position pos in the correct place in the array such that arr from 0 to pos is sorted
    in ascending order

    Args:
        arr (List[int]): input arr
        pos (int): position of the element that needs to be inserted in correct place

    Returns:
        List[int]: _description_
    """
    for i in range(pos, 0, -1):
        if arr[i] < arr[i - 1]:
            swap(arr, i - 1, i)
        else:
            break
    return arr


def swap(arr: List[int], pos1: int, pos2: int):
    """exchanges elements at pos1 and pos2

    Args:
        arr (List[int]): input array
        pos1 (int): first element position
        pos2 (int): second element position

    Returns:
        _type_: _description_
    """
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp

    return arr


arr2 = insertion_sort2([3, 5, 6, 1, 2, 7, 9, 0])

print(arr2)
