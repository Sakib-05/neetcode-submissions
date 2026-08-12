# space max can be O(n)
# initialise is O(1)
# push O(n)
# pop O(1)
class MyStack:

    def __init__(self):
        self.array = [0]*100
        self.top_idx = None
        

    def push(self, x: int) -> None:
        if self.top_idx is None:
            self.top_idx = 0
            self.array[self.top_idx] = x
        else:
            self.top_idx+=1
            self.array[self.top_idx] = x


    def pop(self) -> int:
        res = self.array[self.top_idx]
        self.top_idx -=1
        if self.top_idx < 0: self.top_idx = None
        return res
        

    def top(self) -> int:
        return self.array[self.top_idx]
        

    def empty(self) -> bool:
        return self.top_idx ==None
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()