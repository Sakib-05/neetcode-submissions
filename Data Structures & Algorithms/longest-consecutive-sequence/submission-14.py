class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        ans=1

        nums = set(nums)
        nums = list(nums)
        nums.sort()
        print(nums)

        i=0
        for j in range(1,len(nums)):
            if nums[j] - nums[j-1] ==1:
                if j-i+1 > ans:
                    ans= j-i+1
                
            else:
                if j-i > ans:
                    ans= j-i
                i=j

        return ans





        