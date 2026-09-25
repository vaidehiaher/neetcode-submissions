class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # If s1 is longer, it cannot fit inside s2
        if len(s1) > len(s2):
            return False

        # Frequency arrays for s1 and current window of s2
        count1 = [0] * 26
        count2 = [0] * 26

        # Create the first window
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        # Left boundary of window
        left = 0

        # Move right boundary
        for right in range(len(s1), len(s2)):

            # Current window is a permutation
            if count1 == count2:
                return True

            # Add new character entering window
            count2[ord(s2[right]) - ord('a')] += 1

            # Remove old character leaving window
            count2[ord(s2[left]) - ord('a')] -= 1

            # Move window to the right
            left += 1

        # Check the final window
        return count1 == count2