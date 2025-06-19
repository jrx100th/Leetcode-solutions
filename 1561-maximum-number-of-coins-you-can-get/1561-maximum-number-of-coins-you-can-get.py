class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()

        alice = 0
        me = 0
        bob = 0

        while len(piles) != 0:
            alice += piles.pop()
            me += piles.pop()
            bob += piles.pop(0)

        return me