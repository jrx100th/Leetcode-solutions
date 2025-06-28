class Solution:
    def reverseDegree(self, s: str) -> int:
        
        nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
        nums = nums[::-1]
        alps = list("abcdefghijklmnopqrstuvwxyz")

        dicti = dict(zip(alps,nums))
        n = 0
        for i in range(len(s)):
            n+= (i+1)*dicti[s[i]]
        return n