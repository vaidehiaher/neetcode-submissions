class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        l = 0
        r = len(num) - 1
        while l < r:
            currsum = num[l] + num[r]
            if currsum > target:
                r -= 1
            elif currsum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
        