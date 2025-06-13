class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        ns = str(n)

        product = 1
        plus = 0

        for s in ns:
            product*=int(s)
            plus+=int(s)

        return product-plus