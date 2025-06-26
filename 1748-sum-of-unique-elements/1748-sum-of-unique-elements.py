class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = {}

        for num in nums:
            if num not in unique:
                unique[num] = 0
            unique[num] += 1
        x = 0
        for num in unique:
            if unique[num] == 1:
                x+=num
        return x