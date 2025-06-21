class CustomStack:

    def __init__(self, maxSize: int):
        from collections import deque

        self.stack = deque([])
        self.maxheight = maxSize
        self.height = 0
        

    def push(self, x: int) -> None:
        if self.height < self.maxheight:
            self.stack.append(x)
            self.height += 1
        

    def pop(self) -> int:
        if self.height == 0:
            return -1
        self.height -= 1
        return self.stack.pop()

        

    def increment(self, k: int, val: int) -> None:
        if self.height < k:
            for i in range(len(self.stack)):
                self.stack[i]+=val
        else:
            for i in range(k):
                self.stack[i]+=val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)