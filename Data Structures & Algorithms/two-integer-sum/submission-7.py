class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = {}
        for index, value in enumerate(nums):
            hp[value] = index
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hp and hp[diff] != i:
                if i< hp[diff]:
                    return [i, hp[diff]]
                else:
                    return [hp[diff],i]
        