class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        maxi = None
        mini = None

        if len(s) > len(t):
            maxi = s
            mini = t
        else:
            maxi = t
            mini = s

        for m in maxi:
            if maxi.count(m) != mini.count(m):
                return m
