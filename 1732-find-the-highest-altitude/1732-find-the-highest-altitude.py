class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        resl = [0]
        c = 0
        for al in gain:
            c+=al
            resl.append(c)
        
        return max(resl)