class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        result = []

        def check(number):
            xumber = str(number)
            xylon = 0
            for x in xumber:
                if x != '0':
                    if number%int(x) == 0:
                        xylon+=1
                else:
                    pass

            if xylon == len(xumber):
                return 1
            else:
                return 0

        for i in range(left,right+1):
            y = check(i)
            if y == 1:
                result.append(i)
            else:
                pass

        return result