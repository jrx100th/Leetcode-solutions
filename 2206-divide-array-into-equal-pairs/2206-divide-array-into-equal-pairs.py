class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        mapper = {}
        for num in nums:
            if num not in mapper:
                mapper[num] = 0
            mapper[num] += 1

        for num in nums:
            if mapper[num]%2 != 0 :
                return False
        return True