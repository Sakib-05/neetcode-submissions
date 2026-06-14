class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        res=0

        for num in nums:
            length=1
            if num-1 in st:
                continue
            
            while num + length in st:
                length+=1
            
            if length > res:
                res=length
        
        return res





        