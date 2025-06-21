class Solution:
    def removeStars(self, s: str) -> str:

        
        res = []
        n = 0
        for i in range(len(s)):
            if s[i] != '*':
                res.append(s[i])
            if s[i] == '*':
                if len(res)!=0:
                    res.pop()

        return "".join(res)
                