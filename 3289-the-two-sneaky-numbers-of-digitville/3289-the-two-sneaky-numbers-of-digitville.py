class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        x = set()

        for num in nums:
            if nums.count(num) > 1:
                x.add(num)

        return list(x)