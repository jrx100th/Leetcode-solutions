class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        while len(nums) != 0:
            a = (min(nums))
            nums.remove(min(nums))
            b = (min(nums))
            nums.remove(min(nums))
            l.append(b)
            l.append(a)

        return l