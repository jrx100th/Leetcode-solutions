class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        wordlist = s.split(' ')

        if k >= len(wordlist):
            return s
        else:
            wordlist = wordlist[:k]

            return " ".join(wordlist)