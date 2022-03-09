def insertion_sort(arr: list):
    """Sorts an array in-place

    Args:
        arr (list): array to sort
    """
    
    for j in range(1, len(arr)):
        
        key = arr[j]
        
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        
        arr[i+1] = key
        
def selection_sort(arr: list):
    """Sorts an array by finding first the smallest element of arr 
    and exchanging it with the element in arr[0]. Then find the 
    second smallest element of A, and exchange it with arr[1] and so on.

    Args:
        arr (list): array to sort
    """
    for index1 in range(len(arr) - 1):
        smallest_index = index1
        for index2 in range(index1 + 1, len(arr)):
            if arr[index2] < arr[smallest_index]:
                smallest_index = index2
                
        if index1 != smallest_index:
            key = arr[index1]
            arr[index1] = arr[smallest_index]
            arr[smallest_index] = key
            
            
def find_max_sub_array_v1(arr: list) -> int:
    """Returns the total of the subarray in arr with the heights sum.
    Using dynamic prorgramming

    Args:
        arr (list): input array

    Returns:
        int: highest sum
    """
    
    # 1- start at first element and store it in first position of max_sum
    # 2- move to next element.
    # 3- which is bigger? sum of both? or next element alone?
    # 4- update max_sum arrary with the highest value at the current position
    # 5- goto step 2
    # 6- search max_sum array for highest sum and return
    
    max_sum = []
    
    max_sum.append(arr[0])
    
    for index in range(1, len(arr)):
        max_sum.append(max(arr[index], max_sum[index - 1] + arr[index]))
        
    return max(max_sum)       
    
def find_max_sub_array_v2(arr: list) -> int:
    """Returns the total of the subarray in arr with the highest sum

    Args:
        arr (list): input array

    Returns:
        int: highest sum
    """
    
    global_max_sum = arr[0]
    max_sum = arr[0]
    
    for index in range(1, len(arr)):
        max_sum = max(arr[index], max_sum + arr[index])
        if global_max_sum < max_sum:
            global_max_sum = max_sum
        
    return global_max_sum  
    
    
def find_max_sub_array_v3(arr: list) -> int:
    """find contigious subarray with maximum sum and return the sum.
    This time using Divide and Conquer

    Args:
        arr (list): input array

    Returns:
        int: sum of max sub-array
    """
    
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        lss = arr[0]
        rss = arr[1]
        css = arr[0] + arr[1]
        return max(lss, css, rss)
    else:
        mid = len(arr) // 2 if len(arr) % 2 == 0 else len(arr) // 2 + 1
        lss = find_max_sub_array_v3(arr[:mid])
        rss = find_max_sub_array_v3(arr[mid:])
        
        sm = 0
        rcss = -10000
        for index in range(mid, len(arr)):
            sm += arr[index]
            
            if sm > rcss:
                rcss = sm
                 
        sm = 0
        lcss = -10000
        for index in range(mid-1, -1, -1):
            sm += arr[index]
            
            if sm > lcss:
                lcss = sm
          
        css = rcss + lcss
        
        return max(lss, css, rss)
    
####################################################################
# main()        
#
def main():
    a = [5, 2, 4, 6, 1, 3]
    insertion_sort(a)
    print(a)
    
    b = [6, 5, 4, 3, 2, 1]
    selection_sort(b)
    print(b)
    
    c = [-2,1,-3,4,-1,2,1,-5,4]
    print(find_max_sub_array_v1(c))
    print(find_max_sub_array_v2(c))
    print(find_max_sub_array_v3(c))
    
    d = [5,4,-1,7,8]
    print(find_max_sub_array_v3(d))
    
    e = [-1,0,-2]
    print(find_max_sub_array_v3(e))
    
    f = [-2,3,0,2,-2,3]
    print(find_max_sub_array_v3(f))
    
    g = [3,20,0,-2,-2,1]
    print(find_max_sub_array_v3(g))

if __name__ == "__main__":
    main()
