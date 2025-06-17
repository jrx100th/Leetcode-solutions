class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sing = 0
        doub = 0

        for num in nums:
            if num < 10:
                sing += num
            else:
                doub += num

        return not sing == doub