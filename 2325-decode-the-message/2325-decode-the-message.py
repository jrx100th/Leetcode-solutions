class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        

        keey = []
        seen = set()

        for i in range(len(key)):
            if key[i] != ' ' and key[i] not in seen:
                keey.append(key[i])
                seen.add(key[i])

        
        alps = (sorted(keey))
        res = []
        for letter in message:
            if letter != ' ':
                index = keey.index(letter)
                res.append(alps[index])
            else:
                res.append(' ')

        return "".join(res)