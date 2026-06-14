class MinStack:

    def __init__(self):
        self.stack=[]
        self.small_stack=[]
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.small_stack)>0:
            if val<self.small_stack[-1]:
                self.small_stack.append(val)
            else:
                self.small_stack.append(self.small_stack[-1])
        else:
            self.small_stack.append(val)

        

        

    def pop(self) -> None:
        self.stack.pop()
        self.small_stack.pop()
        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.small_stack[-1]
        
        
