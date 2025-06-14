class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = 0
        for num in nums:
            if num < k:
                n+=1
        return n