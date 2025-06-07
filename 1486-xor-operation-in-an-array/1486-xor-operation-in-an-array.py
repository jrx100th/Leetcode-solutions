class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        # logix : start + 2*i

        nums = []
        num = 0
        for i in range(n):
            nums.append(start+2*i)

        for i in range(len(nums)):
            num^=nums[i]

        return num       
        
        