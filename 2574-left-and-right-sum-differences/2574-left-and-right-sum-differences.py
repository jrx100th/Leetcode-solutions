class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = []
        
        x = 0
        for i in range(len(nums)):
            x += nums[i]
            left.append(x)
        
        right = []

        y = 0
        for i in range(len(nums)-1,-1,-1):
            y += nums[i]
            right.append(y)
        right =  right[::-1]
        res = []

        for i in range(len(nums)):
            res.append(abs(left[i]-right[i]))

        return res