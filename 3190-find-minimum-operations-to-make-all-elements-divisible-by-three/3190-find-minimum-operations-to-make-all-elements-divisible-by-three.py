class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = 0

        for num in nums:
            if num%3 != 0:
                n += 1

        return n