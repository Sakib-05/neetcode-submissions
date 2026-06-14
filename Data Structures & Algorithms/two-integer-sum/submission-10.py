class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = {}
        res = []

        for i,e in enumerate(nums):
            hp[e] = i
        
        for i,e in enumerate(nums):
            diff = target - e
            if diff in hp and hp[diff] != i:
                return [i,hp[diff]] if i< hp[diff] else [hp[diff],i]


        