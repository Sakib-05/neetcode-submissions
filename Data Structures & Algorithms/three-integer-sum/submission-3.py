class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        n=len(nums)
        unique=set()

        # -nums[i] = nums[j] + nums[k]

        for i in range(n):
            target= -1* nums[i]
            l,r = i+1, n-1
            while l<r:
                if nums[l] + nums[r] ==target and str([nums[i],nums[l],nums[r]]) not in unique:
                    res.append([nums[i],nums[l],nums[r]])
                    unique.add(str([nums[i],nums[l],nums[r]]))
                    l-=1
                elif nums[l] + nums[r] <target:
                    l+=1
                else:
                    r-=1        






        return list(res)

        