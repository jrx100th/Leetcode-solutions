class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        count = Counter(nums)
        cands = []
        n = (len(nums)/3)
        for num, count in count.items():
            if count > n:
                cands.append(num)
        return cands