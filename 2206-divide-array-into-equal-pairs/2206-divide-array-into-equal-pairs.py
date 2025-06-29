class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        seen = set()
        pairs = 0

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                seen.remove(num)
                pairs += 1
        if len(seen) != 0:
            return False
        else:
            return pairs*2 == len(nums)