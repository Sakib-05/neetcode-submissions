class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        n=len(nums)

        # -nums[i] = nums[j] + nums[k]

        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            target= -1* nums[i]
            l,r = i+1, n-1
            while l<r:
                if nums[l] + nums[r] ==target:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif nums[l] + nums[r] <target:
                    l+=1
                else:
                    r-=1        






        return list(res)

        