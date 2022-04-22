# write a merge sort function
def merge_sort(arr: list) -> list:
    """Sorts an array of integers in place by recursively splitting the array into two halves and then merging the two
    sorted halves back together in the correct order
    
    Args:
        arr (list): array to sort
        
    Output:
        (list): sorted array
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left: list, right: list) -> list:
    """Merges two sorted arrays into a single sorted array
    
    Args:
        left (list): left sorted array
        right (list): right sorted array
        
    Output:
        (list): merged array
    """
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    result += left[i:]
    result += right[j:]
    return result
