class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}
        s = list(s)

        for num in s:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        
        counter = dict(sorted(counter.items(), key = lambda x:x[1], reverse = True))
        
        res = ""

        for key,value in counter.items():
            st = key*value
            res+=st

        return res


