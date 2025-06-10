class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        scores = []
        for i in range(len(s)-1):
            scores.append(abs(ord(s[i])-ord(s[i+1])))
        
        return sum(scores)