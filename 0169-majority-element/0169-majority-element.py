class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        count = Counter(nums)
        n = len(nums)
        
        for num, count in count.items():
            if count > (n/2):
                return num
        