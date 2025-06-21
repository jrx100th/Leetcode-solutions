class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        
        res = []

        for i in range(len(s)):
            if len(res) == 0:
                res.append(s[i])
            else:
                if res[-1] == s[i]:
                    res.pop()
                else:
                    res.append(s[i])

        return "".join(res)