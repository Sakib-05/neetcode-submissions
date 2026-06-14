class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #lowest buy 
        #highest sell
        l=0
        r=l+1
        profit=0

        while r<len(prices):
            if prices[r] > prices[l]:
                temp = prices[r]-prices[l]
                profit=max(temp,profit)
            else:
                l=r
            r+=1
        
        return profit


        