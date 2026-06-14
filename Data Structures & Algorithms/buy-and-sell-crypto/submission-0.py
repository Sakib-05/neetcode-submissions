class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        l=0
        r=len(prices)-1

        #lowest price to buy
        # highest price to sell

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit= max(prices[j]-prices[i],profit)
        
        return profit
        