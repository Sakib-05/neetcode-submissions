class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # M arrays, each array is length N

        def bs(array,t):
            l=0
            r= len(array)-1
            while l<=r:
                m=(l+r)//2

                if array[m]==target:
                    return m
                elif target> array[m]:
                    l=m+1
                else:
                    r=m-1
            
            return -1

        for row in matrix:
            if bs(row,target) != -1:
                return True

        return False 