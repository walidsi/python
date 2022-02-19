def my_sum(arr: list) -> int:
    if arr == []:
        return 0
    else:
        return arr[0] + my_sum(arr[1:])

def my_count(arr: list) -> int:
    if arr == []:
        return 0
    else:
        return 1 + my_count(arr[1:])

def my_max(arr: list) -> int:
    if arr == []:
        return None
    elif len(arr) == 1:
        return arr[0]

    inner_max  = my_max(arr[1:])

    max_num = arr[0] if arr[0] > inner_max else inner_max

    return max_num

def my_binary_search(arr: list, num: int):
    if arr == []:
        return None

    low, high = 0, len(arr)

    mid = (low + high) // 2

    if num < arr[mid]:
        high = mid
    elif num > arr[mid]:
        low = mid + 1
    else:
        return mid

    index = my_binary_search(arr[low:high], num)

    if index == None:
        return None
    else:
        return index + low
    
    
def quick_sort(arr: list):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return  quick_sort(less) + [pivot] + quick_sort(greater)
    
def minmax(nums: list) -> tuple:
    """Finds the minimum and max values in a list.
    Assumes list nums contains at least one element.

    Args:
        nums (list): input list

    Returns:
        tuple: minimum and maximum values
    """
    
    # Finds minimum and maximum values in a list using divide and conquer
    
    #assert len(nums) >= 1, "nums cannot be empty"
    if nums == []:
        return (None, None)
    
    if len(nums) == 1:
        return (nums[0], nums[0])
    elif len(nums) == 2:
        return (nums[0], nums[1]) if nums[0] < nums[1] else (nums[1], nums[0])
    
    low = 0
    high = len(nums)
    mid = (low + high) // 2
    
    tuple1 = minmax(nums[0:mid])
    tuple2 = minmax(nums[mid:high])
    
    min = tuple1[0] if tuple1[0] < tuple2[0] else tuple2[0]
    max = tuple1[1] if tuple1[1] > tuple2[1] else tuple2[1]
    
    return (min, max)


def main():
    print(my_sum([1, 2, 3, 4, 5]))
    print(my_count([1, 2, 3, 4, 5]))
    print(my_max([]))
    print(my_binary_search([1, 2, 3, 4, 5, 6, 7], 6))
    print(quick_sort([-1, 2, -7, 3, 0, 5, -200, 1000, -100, 1, 2]))
    
    print(minmax([1, 2, 3, 4, 5, 6]))
    print(minmax([1, 2, 3, 4, 5, 6, 7]))
    print(minmax([1, 2]))
    print(minmax([1]))
    print(minmax([1, 2, -1, -33, 4, 5, 6, 7, 2, 5, -12, 19, 100, 2, 3, 66]))
    print(minmax([]))


if __name__ == '__main__':
    main()



