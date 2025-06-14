class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = []

        for num in nums:
            n.append(num**2)

        n.sort()

        return n