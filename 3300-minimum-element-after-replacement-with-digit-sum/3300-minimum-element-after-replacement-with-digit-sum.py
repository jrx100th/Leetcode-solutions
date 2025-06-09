class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = ""
        added = []
        for num in nums:
            x = str(num)
            y = 0
            for i in range(len(x)):
                y += int(x[i])
            added.append(y)

        return min(added)
                

