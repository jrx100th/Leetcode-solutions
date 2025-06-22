class Solution:
    def countKeyChanges(self, s: str) -> int:

        s = s.lower()
        stack = []
        n = 0
        for i in range(len(s)):
            if len(stack) ==0:
                stack.append(s[i])
            else:
                if stack[-1] != s[i]:
                    n+=1
                    stack.append(s[i])


        return n