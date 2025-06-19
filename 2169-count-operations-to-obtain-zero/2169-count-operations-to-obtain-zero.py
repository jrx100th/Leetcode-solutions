class Solution:
    def countOperations(self, num1: int, num2: int) -> int:

        x = 0

        while num1*num2 != 0:
            if num1>=num2:
                num1-=num2
                x+=1
            else:
                num2-=num1
                x+=1

        return x