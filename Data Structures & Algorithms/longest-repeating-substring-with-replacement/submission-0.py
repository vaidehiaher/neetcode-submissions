class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0              # Left side of sliding window
        max_freq = 0           # Highest character frequency
        max_len = 0            # Longest valid window
        count = [0] * 26       # Frequency of A-Z

        for right in range(len(s)):    # Expand window from right

            index = ord(s[right]) - ord('A')
            count[index] += 1           # Add current character

            max_freq = max(max_freq, count[index])

            # If too many replacements are needed,
            # shrink the window
            while (right - left + 1) - max_freq > k:

                index = ord(s[left]) - ord('A')
                count[index] -= 1       # Remove left character

                left += 1               # Move left pointer

            # Current window is valid
            max_len = max(max_len, right - left + 1)

        return max_len
        