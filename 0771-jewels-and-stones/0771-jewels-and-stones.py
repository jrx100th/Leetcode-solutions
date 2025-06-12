class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        n = 0

        for stone in stones:
            if stone in jewels:
                n+=1
        return n