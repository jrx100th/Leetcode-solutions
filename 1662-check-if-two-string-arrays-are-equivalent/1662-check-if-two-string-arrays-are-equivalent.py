class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        x = ""

        for word in word1:
            x+=word
        y = ""

        for word in word2:
            y+=word

        return x==y