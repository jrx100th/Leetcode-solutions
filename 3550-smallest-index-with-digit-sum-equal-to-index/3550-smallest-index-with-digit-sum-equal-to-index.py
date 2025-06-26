class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for index, value in enumerate(nums):
            digit_sum = 0
            while value:
                digit_sum += value%10
                value //=10
            if digit_sum == index:
                return index
        return -1