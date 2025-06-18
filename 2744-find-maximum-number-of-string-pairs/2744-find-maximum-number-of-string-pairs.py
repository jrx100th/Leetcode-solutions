class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        n = 0

        for word1 in words:
            for word2 in words:
                if word1 == word2[::-1]:
                    n+=1

        return n//2