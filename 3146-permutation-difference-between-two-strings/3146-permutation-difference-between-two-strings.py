class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res = 0
        for ch in s:
            res += abs(s.index(ch) - t.index(ch))
        return res