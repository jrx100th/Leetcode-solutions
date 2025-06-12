class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        t = 0
        l = []
        for num in nums:
            t+=num
            l.append(t)

        return l