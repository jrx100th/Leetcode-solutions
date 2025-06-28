class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        mapper = {}

        for num in nums:
            mapper[num] = 1

        for num in nums:
            num = int(str(num)[::-1])
            if num not in mapper:
                mapper[num] = 1
            else:
                mapper[num]+=1

        return len(mapper)