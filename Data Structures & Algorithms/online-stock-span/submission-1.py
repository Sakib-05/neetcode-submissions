class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        if len(self.stack) == 0:
            self.stack.append((price,1))
            return 1
        
        res = 1

        while self.stack and self.stack[-1][0] <= price:
            res+=self.stack[-1][1]
            self.stack.pop()
        
        self.stack.append((price,res))
        return res



        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)