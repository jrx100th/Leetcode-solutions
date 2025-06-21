class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []

        for i in range(len(s)):
            if s[i] != '#':
                stack1.append(s[i])
            else:
                if len(stack1) != 0:
                    stack1.pop()

        stack2 = []

        for j in range(len(t)):
            if t[j] != '#':
                stack2.append(t[j])
            else:
                if len(stack2) != 0:
                    stack2.pop()

        return "".join(stack1) == "".join(stack2)