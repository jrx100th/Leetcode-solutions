class Solution:
    def similarPairs(self, words: List[str]) -> int:
        dicti = {}
        for word in words:
            word = "".join(sorted(set(word)))
            if word not in dicti:
                dicti[word] = 0
            dicti[word] += 1

        n = 0
        
        for x in dicti:
            count = dicti[x]
            n += count*(count-1)//2

        return n
        
        