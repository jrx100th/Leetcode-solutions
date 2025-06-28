class Solution:
    def sortSentence(self, s: str) -> str:
        
        s = s.split(" ")
        res = " "*(len(s)+len(s)-1)
        res = list(res)

        for word in s:
            pos = int(word[-1])+int(word[-1])-1
            res[pos-1] = word[:-1]
        return  "".join(res)