class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        mapper = {}
        for letter in s:
            if letter not in mapper:
                mapper[letter] = 0
            mapper[letter] += 1

        for letter in t:
            if letter not in mapper:
                return False
            if letter in mapper:
                mapper[letter] -= 1

        mapper =  list(mapper.values())

        for num in mapper:
            if num != 0:
                return False
        return True