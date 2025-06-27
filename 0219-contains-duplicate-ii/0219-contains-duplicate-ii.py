class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapper = {}

        for index, value in enumerate(nums):
            if value in mapper and abs(index-mapper[value]) <= k:
                return True
            mapper[value] = index
        return False