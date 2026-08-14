class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # O(n) time and (1) space

        # add nums2 elements into nums1 from m to m+n

        n1 = nums1[:m]

        l,r = 0,0
        i=0

        while l<m and r<n:
            if n1[l] <= nums2[r]:
                nums1[i] = n1[l]
                l+=1
            
            else:
                nums1[i] = nums2[r]
                r+=1
            

            i+=1
        

        
        if l <m:
            for i in range(i,len(nums1)):
                nums1[i] = n1[l]
                l+=1
        
        else:
            for i in range(i,len(nums1)):
                nums1[i] = nums2[r]
                r+=1

        






    




        
