class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        if len(self.stack) ==0: 
            self.stack.append(price)
            return 1
        
        n = len(self.stack)
        res = 1
        for i in range(n-1, -1,-1):
            if self.stack[i] <= price:
                res+=1
            else:
                break
        self.stack.append(price)
        return res

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)