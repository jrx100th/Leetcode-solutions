class Solution:
    def countEven(self, num: int) -> int:
        # digital sum does'nt work here

        def fun1(nums):
            x = 0
            while nums:
                x+= nums%10
                nums//=10

            return x

        n = 0

        for i in range(1, num+1,1):
            if fun1(i)%2 == 0:
                n+=1
        return n            