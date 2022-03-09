def max_sub_array(nums) -> int:
    """Given an integer array nums, find the contiguous subarray (containing at least one number) 
    which has the largest sum and return its sum. A subarray is a contiguous part of an array.

    Args:
        nums (list): integer array

    Returns:
        int: sum of largest contiguous part of the array
        
    Example:
        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: [4,-1,2,1] has the largest sum = 6.
    """
    
    #solution using brute force
    global_sum = nums[0]
    
    for index1 in range(len(nums)):
        local_sum = nums[index1]
        
        if local_sum > global_sum:
            global_sum = local_sum
        
        for index2 in range(index1 + 1, len(nums)):
            local_sum += nums[index2]
            
            if local_sum > global_sum:
                global_sum = local_sum
                
    return global_sum

print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
print(max_sub_array([0, 1, 2, 3, 4, 5, 6]))
print(max_sub_array([1, 100]))
print(max_sub_array([99]))
print(max_sub_array([-2,1]))
