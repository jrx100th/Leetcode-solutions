class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ret = {}

        for value, weight in items1:
            if value not in ret:
                ret[value] = weight
            else:
                ret[value] += weight
        for value, weight in items2:
            if value not in ret:
                ret[value] = weight
            else:
                ret[value] += weight

        ret = sorted(ret.items(), key = lambda x:x)
        return ret