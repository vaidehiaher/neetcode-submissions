class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for word in strs:
            freq = [0]*26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            mp[tuple(freq)].append(word)
        return list(mp.values())