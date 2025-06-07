class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """from collections import Counter
        count = Counter(nums)
        n = len(nums)
        
        for num, count in count.items():
            if count > (n/2):
                return num"""

        candidate = None
        nums.sort()
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
        