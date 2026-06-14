class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 +nums2
        merged.sort()
        print(merged)
        # len 5
        # 0,1,2,3,4
        # l=0
        # r=5
        # m = 2
        l=0
        r=len(merged)-1
        mid=(l+r)//2

        if len(merged) %2 ==0:
            
            a= merged[mid]
            b= merged[mid+1]
            return (a+b)/2
        return merged[mid]
        