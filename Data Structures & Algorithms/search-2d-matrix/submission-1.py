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

        # bs for finding the correct row

        l=0
        r=len(matrix)-1
        row=[]
        while l<=r:
            # mth row
            m=(l+r)//2
            if target>=matrix[m][0] and target <= matrix[m][len(matrix[m])-1]:
                row=matrix[m]
                break
            elif target <matrix[m][0]:
                r=m-1
            else:
                l=m+1

        if len(row) ==0 : return False

        if bs(row, target) !=-1:
            return True

        return False 