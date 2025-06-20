class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        seen = set()

        res = []

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                res.append(num)

        return res