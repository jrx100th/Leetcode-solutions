class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = Counter(jewels)
        n = 0

        for stone in stones:
            if stone in count:
                n+=1
        return n