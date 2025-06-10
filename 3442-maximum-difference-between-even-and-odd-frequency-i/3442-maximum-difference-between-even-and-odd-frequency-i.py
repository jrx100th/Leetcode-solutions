class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """

        st = set(s)
        st = list(st)

        scores = []

        for i in range(len(st)):
            scores.append(s.count(st[i]))

        max_even = max(scores)
        max_odd = 0

        for score in scores:
            classic = 0
            if score%2 == 1:
                classic = score
            if classic > max_odd:
                max_odd = classic

        for score in scores:
            classic = max(scores)
            if score%2 == 0:
                classic = score
            if classic < max_even:
                max_even = classic

        return max_odd - max_even
        