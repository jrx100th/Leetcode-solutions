class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = 0
        for num in nums:
            n+=1
            if num == target:
                return n-1
        return -1