class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        v = 0
        c = 0
        
        dicti = {}

        for x in s:
            if x in dicti:
                dicti[x] += 1
            else:
                dicti[x] = 1
        
        dicti = dict(sorted(dicti.items(), key = lambda x:x[1], reverse = True))
        
        for letter in dicti:
            if letter in vowels:
                if dicti[letter] > v:
                    v = dicti[letter]
            else:
                if dicti[letter] > c:
                    c = dicti[letter]

        return c+v