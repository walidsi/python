def binary_search(arr: list, item: int):
    """Searches for a integer in a sorted array of integers

    Args:
        arr (list): list of sorted elements to search in
        item (int): integer to search for
        
    Returns:
        Position of item if found, otherwise None
    """
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] > item:
            high = mid - 1
        elif arr[mid] < item:
            low = mid + 1
        else:
            return mid
    
    return None
