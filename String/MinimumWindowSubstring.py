from collections import Counter
from math import inf
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        needed = Counter(t)
        current = {}
        count, target = 0, len(needed)
        l = 0
        
        pointers = [0, inf]
        for r in range(len(s)):
            c = s[r]
            if c in needed:
                current[c] = current.get(c, 0) + 1
                if current[c] == needed[c]:
                    count += 1
#           While substring is valid
            while count == target:
                if r-l < pointers[1] - pointers[0] :
                    pointers[0], pointers[1] = l, r
                if s[l] in needed:
                    current[s[l]] -= 1
                    if current[s[l]] < needed[s[l]]:
                        count -= 1
                l += 1
        if pointers[1] == inf:
            return ""
        return s[pointers[0]:pointers[1] +1]
sol = Solution()
print(sol.minWindow("aa","aa"))
