class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        n=len(temperatures)

        for i in range(n):
            days=0
            for j in range(i+1,n):
                if temperatures[i] < temperatures[j]:
                    days= j-i
                    print(days)
                    break

            res.append(days)
        
        return res

        