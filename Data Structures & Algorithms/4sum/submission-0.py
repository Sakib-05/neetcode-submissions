class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:


        res = []

        nums.sort()
        n = len(nums)
        # indices i,j,l,r
        for i in range(n-3):
            a = nums[i]

            for j in range(i+1,n-2):
                b = nums[j]

                l,r = j+1,n-1
                while l<r:
                    # while l<r and nums[l]==nums[l+1]:
                    #     l+=1
                    
                    # while r>l and nums[r]==nums[r-1]:
                    #     r-=1
                    c = nums[l]
                    d = nums[r]
                    total = sum([a,b,c,d])
                    if total == target and [a,b,c,d] not in res:
                        res.append([a,b,c,d])
                    elif total > target:
                        r-=1
                    else:
                        l+=1
                    
                    
        return res
