class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        mapper = dict(zip(heights, names))
        mapper = dict(sorted(mapper.items(), key = lambda x:x[0], reverse = True))
        
        return [i for i in mapper.values()]

        