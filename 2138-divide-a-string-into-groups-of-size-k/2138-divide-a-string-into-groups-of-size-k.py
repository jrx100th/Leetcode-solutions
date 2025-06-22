class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        res = []

        if len(s)%k == 0:
            for i in range(0,len(s),k):
                res.append(s[i:k+i])
        else:
            for i in range(0,len(s),k):
                res.append(s[i:k+i])
            b = k-len(res[-1])
            res[-1] += b*fill

        return res