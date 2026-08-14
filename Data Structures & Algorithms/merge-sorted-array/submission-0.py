class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # O(n) time and (1) space

        # add nums2 elements into nums1 from m to m+n

        for i in range(n):
            nums1[m+i] = nums2[i]
        
        nums1.sort()





    




        
