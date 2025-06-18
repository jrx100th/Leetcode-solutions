class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        if ch not in word or len(word) == 1:
            return word
        
        res = []

        for i in range(len(word)):
            if word[i] == ch:
                res.append(word[i])
                break
            res.append(word[i])
        
        word = list(word)

        result = res[::-1] + word[len(res):]

        return ''.join(result)
