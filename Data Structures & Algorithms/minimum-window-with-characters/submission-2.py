class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        have = {}
        have_count = 0
        need_count = len(need)

        left = 0
        min_len = float("inf")
        result = ""

        for right in range(len(s)):
            char = s[right]
            have[char] = have.get(char, 0) + 1

            if char in need and have[char] == need[char]:
                have_count += 1

            while have_count == need_count:

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                left_char = s[left]
                have[left_char] -= 1

                if left_char in need and have[left_char] < need[left_char]:
                    have_count -= 1

                left += 1

        return result
        