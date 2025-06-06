class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        o = 0
        n = bin(n)
        for i in range(len(n)):
            if n[i] == '1':
                o += 1
        return o
        