class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max = 0
        for account in accounts:
            if sum(account) > max:
                max = sum(account)
        return max
