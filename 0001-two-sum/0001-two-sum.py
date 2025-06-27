class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dicti = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dicti:
                return [dicti[complement],i]
            dicti[nums[i]] = i
        return []