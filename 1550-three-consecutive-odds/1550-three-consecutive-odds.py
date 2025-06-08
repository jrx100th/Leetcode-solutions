class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(1, len(arr)-1):
            if arr[i-1]%2 == 1 and arr[i]%2 == 1 and arr[i+1]%2 == 1:
                return True
        return False


        ## can use a sliding window,
        ## tinker with the loop ranges
        # like min+1 and max-1 and traversing through it