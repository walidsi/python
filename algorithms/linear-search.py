def linear_search(arr: list, length: int, x: int) -> int:
    """search an array for an integer
    
    Args:
        arr (list): array to search
        length (int): length of array
        x (int): integer to search for
        
    Output:
        (int): index of integer in array or -1 if not found
    """

    answer = -1

    for index in range(0, length):
        if arr[index] == x:
            answer = index

    return answer


arr = [3, 1, 4, 5, 6, 3, 1, 2, 9, 8]
print(linear_search(arr, len(arr), 1))


def better_linear_search(arr: list, length: int, x: int) -> int:
    """search an array for an integer
    
    Args:
        arr (list): array to search
        length (int): length of array
        x (int): integer to search for
        
    Output:
        (int): index of integer in array or -1 if not found
    """

    for index in range(0, length):
        if arr[index] == x:
            return index
    return -1


def sentinel_linear_search(arr: list, length: int, x: int) -> int:
    """_summary_
    
    Args:
        arr (list): array to search
        length (int): length of array
        x (int): integer to search for
        
    Output:
        (int): index of integer in array or -1 if not found
    """

    last = arr[length - 1]
    arr[length - 1] = x

    index = 0

    while arr[index] != x:
        index += 1

    arr[length - 1] = last  # restore the last element

    if index < length - 1 or arr[length - 1] == x:
        return index

    return -1
