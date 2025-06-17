class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = 0

        for num in nums:
            if len(str(num))%2 == 0:
                n+=1

        return n