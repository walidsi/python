fib_cache = {}

def fib(n) -> int:
    """Calculates fibonaci of n, top-down approach using recursion

    Args:
        n (int): number
    Return:
        Fibonanci of n
    """
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        try:
            return fib_cache[n]
        except:
            fib_cache[n] = fib(n-1) + fib(n-2)
            return fib_cache[n]
        
def fib_2(n) -> int:
    """Calculates fibonaci of n

    Args:
        n (int): number
    Returns:
        Fibonanci of n
    """
    
    # Uses bottom-up approach using iteration to calculate fibonacci of n
    fib_table = {}
    
    fib_table[0] = 0
    fib_table[1] = 1
    
    for i in range(2, n+1):
        fib_table[i] = fib_table[i-1] + fib_table[i-2]
        
    return fib_table[n]

def fib_3(n) -> int:
    """Calculates fibonaci of n

    Args:
        n (int): number
    Returns:
        int: fibonnaci of n
    """
    
    # Uses hash table to store intermediate fibonaci values
    if n in fib_cache:
        return fib_cache[n]
    else:
        ans = fib_3(n-1) + fib_3(n-2)
        fib_cache[n] = ans
        return ans

def is_palindrome(s: str) -> bool:
    """Checks if string s is a palindrome

    Args:
        s (str): input string
    Returns:
        bool: True if palindrome, False otherwise
    """
    
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])


def is_palindrome2(s: str) -> bool:
    """Checks if string s is a palindrome

    Args:
        s (str): input string
    Returns:
        bool: True if palindrome, Fale otherwise
    """
    
    try:
        if s[0] == s[-1] and is_palindrome(s[1:-1]):
            return True
    except:
        return True
    
    return False

def search(L, e):
    """Assumes L is a list, the elements of which are in
    ascending order.
    Returns True if e is in L and False otherwise"""
    def bSearch(L, e, low, high):
        #Decrements high - low
        if high == low:
            return L[low] == e
        
        mid = (low + high) // 2
        
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)
    
    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)

def merge_sort(nums: list) -> list:
    """Sorts a list of numbers

    Args:
        nums (list): input array to be sorted
    Returns:
        list: a new sorted array
    """
    
    # Sorts a list using divide and conquer
    
    if len(nums) == 1:
        return nums[:]
    elif len(nums) == 2:
        if nums[0] > nums[1]:
            return [nums[1], nums[0]]
        else:
            return nums[:]
        
    low = 0
    high = len(nums)
    mid = (low + high) // 2
    
    nums1 = merge_sort(nums[low:mid])
    nums2 = merge_sort(nums[mid:high])
    
    # Now both nums1 and nums2 are sorted. Time to merge them.
    # Loop comparing nearest element from nums1 to nearest from nums2, 
    # and copy the least of them to nums_sorted.
    # Repeat until one of the two lists is exhausted.
    
    nums_sorted = [] # merged sorted list
    
    index1 = 0 # index to keep track of next item to check from nums1
    index2 = 0 # index to keep track of next item to check from nums2
    
    while index1 < len(nums1) and index2 < len(nums2):
        if nums1[index1] < nums2[index2]:
            nums_sorted.append(nums1[index1])
            index1 += 1 #next index to check in nums1
        else:
            nums_sorted.append(nums2[index2])
            index2 += 1 # next index to check in nums2
    
    # Now at least one of the two lists is exhausted, so just need to copy
    # the remaining items from the non-empty list (if any) to nums_sorted
    while index1 < len(nums1):
        nums_sorted.append(nums1[index1])
        index1 += 1
    
    while index2 < len(nums2):
        nums_sorted.append(nums2[index2])
        index2 += 1
        
    return nums_sorted

##############################################################
# main()
#
def main():
    print(search([1, 2, 3, 4, 5, 6], 0))
    print(search([1, 2, 3, 4, 5, 6], 7))
    print(search([1, 2, 3, 4, 5, 6], 2))
    print(search([1, 2, 3, 4, 5, 6], 5))
    print(search([1, 2, 3, 4, 5, 6], 3))
    print(search([1, 2, 3, 4, 5, 6], 4))

    print(fib(120))
    print(fib_2(120))
    print(fib_3(120))
    
    print(is_palindrome("eve"))
    print(is_palindrome("eve and adam"))

    nums = [2, 1, 3, -50, -100, 2, 5, 100, 1]
    nums_sorted = merge_sort(nums)
    print(nums)
    print(nums_sorted)
    
if __name__ == "__main__":
    main()
