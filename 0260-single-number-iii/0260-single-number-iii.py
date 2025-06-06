class Solution(object):
    def singleNumber(self, nums):
        from collections import Counter
        count = Counter(nums)
        l = []
        for num, count in count.items():
            if count == 1:
                l.append(num)
        return l
        