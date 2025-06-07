class Solution(object):
    def triangleType(self, num):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        num.sort()
        if num[0] == num[1] == num[2]:
            return "equilateral"
        else:
            if num[2] >= num[1]+num[0]:
                return "none"
            elif num[0] != num[1] != num[2]:
                return "scalene"
            else:
                return "isosceles"