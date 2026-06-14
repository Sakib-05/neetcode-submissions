class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i] ==nums[i-1]:
                continue
            target = -nums[i]
            j = i+1
            # while nums[j]==nums[j+1]:
            #     j+=1
            
            k=len(nums)-1

            # while nums[k]==nums[k-1]:
            #     k-=1
            
            while j<k:
                jk_sum = nums[j]+nums[k]

                if jk_sum ==target:
                    res.append([nums[i],nums[j], nums[k]])
                    j+=1
                    while nums[j] ==nums[j-1] and j<k:
                        j+=1
                elif jk_sum > target:
                    k-=1
                else:
                    j+=1


        return res