class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
        res = [0,0]
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num]+=1
        
        """for num in counter:
            if counter[num] < 2:
                res[1]+=counter[num]
            if counter[num] >= 2:
                res[]"""
        
        for num in counter:
            if counter[num] >= 2:
                res[0] += counter[num]//2
        res[1] += len(nums)-(res[0]*2)

        return res