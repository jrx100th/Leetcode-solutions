class Solution(object):
    def singleNumber(self, nums):
        from collections import Counter
        count = Counter(nums)
        for num, count in count.items():
            if count == 1:
                return num
        