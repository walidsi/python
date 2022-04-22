def insertion_sort(arr: list):
    """Sorts an array inplace in ascending order by scanning the array elements one by one starting
    from position 1 and moving it to the correct position in the array by comparing it to all the elements
    before it

    Args:
        arr (list): array to sort
    """
    g_curr = 1
    length = len(arr)
    while g_curr < length:
        curr = g_curr
        while curr > 0 and arr[curr] < arr[curr-1]:
            temp = arr[curr-1]
            arr[curr-1] = arr[curr]
            arr[curr] = temp
            curr -= 1
        g_curr += 1


arr = [3, 1, 4, 5, 6, 3, 1, 2, 9, 8]
insertion_sort(arr)
print(arr)


def selection_sort(arr: list):
    """Sorts an array inplace in ascending order by scanning the array elements one by one putting the smallest
    element at the beginning of the array, then scanning again to put the second smallest element in second position,
    and so on until the array is sorted

    Args:
        arr (list): array to sort
    """
    for index1 in range(0, len(arr)):
        smallest_index = index1
        for index2 in range(index1+1, len(arr)):
            if arr[index2] < arr[smallest_index]:
                smallest_index = index2
        if smallest_index != index1:
            tmp = arr[index1]
            arr[index1] = arr[smallest_index]
            arr[smallest_index] = tmp


arr = [3, 1, 4, 5, 6, 3, 1, 2, 9, 8]
selection_sort(arr)
print(arr)


def bubble_sort(arr: list):
    """Sorts the array in place. Repeatedly swapping adjacent elements that are in the wrong order until there 
    are no more swaps to do and the array is sorted

    Args:
        arr (list): array to sort
    """
    while True:
        swaps = False
        for i in range(0, len(arr) - 1):
            if arr[i+1] < arr[i]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
                swaps = True
        if swaps == False:
            break


arr = [3, 1, 4, 5, 6, 3, 1, 2, 9, 8]
bubble_sort(arr)
print(arr)


def count_sort(arr: list) -> list:
    """Sorts an array of integers in place by counting the number of occurrences of each integer in the array and then
    generating a new array with the same length as the original array and placing the integers in the correct order
    
    Args:
        arr (list): array to sort
        
    Output:
        (list): sorted array
    """
    count = [0] * (max(arr) + 1)

    for i in range(0, len(arr)):
        count[arr[i]] = count[arr[i]] + 1

    sorted_arr = []

    for i in range(0, len(count)):
        for j in range(0, count[i]):
            sorted_arr.append(i)

    return sorted_arr


arr = [3, 1, 4, 5, 6, 3, 1, 2, 9, 8]
print(count_sort(arr))
