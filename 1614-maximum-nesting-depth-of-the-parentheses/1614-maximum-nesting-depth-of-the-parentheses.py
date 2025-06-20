class Solution:
    def maxDepth(self, s: str) -> int:
        n = 0
        x = []
        for i in s:
            if i == '(':
                n+=1
            if i == ')':
                n-=1
            else:
                pass
            x.append(n)
        return max(x)