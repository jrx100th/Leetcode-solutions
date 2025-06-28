class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            seen.add(num)

        for num in nums:
            num = int(str(num)[::-1])
            seen.add(num)

        return len(seen)