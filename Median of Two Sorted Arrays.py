from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two sorted arrays
        # Complexity: O(m + n) for concatenating the two arrays
        # `nums1 + nums2` creates a new array with size m + n
        merged = sorted(nums1 + nums2)

        # Sorting the merged array
        # Complexity: O((m + n) log (m + n)) for sorting the merged array
        # The sorting operation is the most time-consuming part of this function

        # Find the median
        n = len(merged)  # O(1), just accessing the length of the merged array

        if n % 2 == 1:
            # If odd, return the middle element
            # Accessing an element from the list is O(1)
            return float(merged[n // 2])
        else:
            # If even, return the average of the two middle elements
            # Accessing and calculating the average of two elements is O(1)
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0

        # Overall complexity:
        # Time complexity: O((m + n) log (m + n)) due to the sorting step
        # Space complexity: O(m + n) due to the storage of the merged array
