class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        es = sum(nums)
        ds = 0
        for num in nums:
            for digit in str(num):
                ds+=int(digit)

        return abs(es-ds)