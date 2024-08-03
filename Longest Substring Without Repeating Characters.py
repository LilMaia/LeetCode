class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time Complexity: O(n)
        The function processes each character in the string once with the sliding window technique.

        Space Complexity: O(min(n, m))
        Where n is the length of the input string and m is the character set size (which is fixed to 128 in the case of ASCII).

        The space complexity is determined by the size of the set used to store the unique characters in the current window.
        """
        # Initialize the set to store unique characters in the current window
        char_set = set()
        # Initialize the left pointer of the window and the maximum length of the substring
        left = 0
        max_length = 0

        # Iterate over each character in the string using the right pointer
        for right in range(len(s)):
            # If the character is already in the set, remove characters from the left until it's removed
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Add the current character to the set
            char_set.add(s[right])
            # Update the maximum length of the substring
            max_length = max(max_length, right - left + 1)

        return max_length
