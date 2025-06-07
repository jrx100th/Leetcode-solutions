class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        total = 0
        while mainTank >= 5 and additionalTank > 0:
            mainTank -= 5
            total += 5
            mainTank +=1
            additionalTank -= 1
        total += mainTank
        return total*10