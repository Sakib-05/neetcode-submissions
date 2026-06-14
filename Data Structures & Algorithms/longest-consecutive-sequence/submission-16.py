class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        res=0

        for num in nums:
            if num -1 in unique:
                continue
            
            length=0
            while num + length in unique:
                length+=1
            res=max(res,length)
        
        return res

        