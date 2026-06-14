class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = {}
        res = []
        for i,e in enumerate(nums):
            hp[e] = i
        
        for i in range(len(nums)):
            diff = target -nums[i]
            if diff in hp and hp[diff] != i:
                res = [i,hp[diff]] if i<hp[diff] else [hp[diff],i]
         

        
        return res