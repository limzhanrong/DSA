class Solution:
    # Uses a dictionary as a sliding window/substring.

    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = {}
        longest = 0

        l = 0
        for r in range(len(s)):
            if s[r] in hmap:
                while s[r] in hmap:
                    hmap.pop(s[l])
                    l += 1
            hmap[s[r]] = True
            longest = max(longest, len(hmap))

        return longest