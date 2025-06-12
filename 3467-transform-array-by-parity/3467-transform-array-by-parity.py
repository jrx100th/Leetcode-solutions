class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        r = []
        for num in nums:
            if num%2 == 0:
                r.append(0)
            else:
                r.append(1)
        r.sort()
        return r