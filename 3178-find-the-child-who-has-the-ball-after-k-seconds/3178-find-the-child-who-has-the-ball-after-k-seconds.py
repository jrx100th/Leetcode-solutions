class Solution(object):
    def numberOfChild(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        n = n-1
        rounds = k//n
        rem = k%n

        if rounds%2 == 0:
            return rem
        else:
            return n-rem

        