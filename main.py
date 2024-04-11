from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_indices = {}  # Dictionary to store the indices of numbers
    
    # Iterate through the array
    for i, num in enumerate(nums):
        complement = target - num  # Calculate the complement
        
        # Check if the complement exists in the dictionary
        if complement in num_indices:
            # If found, return the indices of the current number and its complement
            return [num_indices[complement], i]
        
        # If the complement doesn't exist in the dictionary, store the index of the current number
        num_indices[num] = i
    
    # If no solution is found, return an empty list
    return []