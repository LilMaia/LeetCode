class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping of Roman numerals to their integer values
        roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        prev_value = 0
        # Iterate over each character in the Roman numeral string
        for char in reversed(s):
            value = roman_values[char]
            # If the current value is less than the previous value, subtract it
            if value < prev_value:
                total -= value
            else:
                total += value
            # Update the previous value
            prev_value = value
        return total
