from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Initialize the hash map to store numbers and their indices

        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement of the current number

            if complement in num_map:  # Check if the complement exists in the hash map
                return [
                    num_map[complement],
                    i,
                ]  # Return the indices of the complement and the current number

            num_map[num] = i  # Add the current number and its index to the hash map

        return (
            []
        )  # This line is not actually needed since the problem guarantees one solution


# Complexity:
# Time Complexity: O(n)
# Space Complexity: O(n)

# Space Complexity
# The space complexity is determined by the space needed to store the num_map dictionary. In the worst case, where all elements are unique, the dictionary will have n key-value pairs.
