class Solution:
    def countDigits(self, num: int) -> int:
        
        sn = str(num)

        n = 0

        for s in sn:
            if num%int(s) == 0:
                n+=1

        return n