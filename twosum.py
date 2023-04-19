"""
An algorithm that takes a list and a target number, and returns
two unique indices that add up to that number.
"""
def twoSum(nums, target):
    # keep track of where we are at (no need to use .index())
    i_index = 0
    j_index = 0

    # O(n^2 due to the double for loop)
    for i in nums:
        i_index += 1
        for j in nums:
            j_index += 1
            # test if it's the same element
            if i_index == j_index:
                continue
            elif i + j == target:
                # have to subtract one from each
                return [i_index-1, j_index-1]
        
        # reset the j index
        j_index = 0