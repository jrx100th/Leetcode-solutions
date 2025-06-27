class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        while "" in s:
            s.remove("")
        if s == []:
            return 0
        return len(s[-1])