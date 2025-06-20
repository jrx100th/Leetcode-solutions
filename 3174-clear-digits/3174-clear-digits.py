class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = []
        

        
        count = 0
        for i in range(len(s)):
            if s[i].isalpha():
                stack.append(s[i])
                count += 1
            if s[i].isnumeric():
                if len(stack) != 0:
                    stack.pop()
                    count -= 1

        return "".join(stack)