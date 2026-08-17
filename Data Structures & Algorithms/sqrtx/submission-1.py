class Solution:
    def mySqrt(self, x: int) -> int:
        # l, r = 0, x
        # res = 0
        # while l <= r:
        #     m = (l + r) // 2
        #     # res = x//m

        #     if (m * m <= x) and (x <= (m + 1) * (m + 1)):
        #         return m

        #     elif (x < m * m) and (x <= (m + 1) * (m + 1)):
        #         r = m - 1
        #     else:
        #         l = m + 1

        res = 0
        i=1
        while i>0:
            if i*i == x:
                return i
            if i*i <x:
                res = i
            else:
                return res
            
            i+=1



        return res
