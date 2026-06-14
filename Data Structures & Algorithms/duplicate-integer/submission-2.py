class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hp = {}

        for num in nums:
            if num not in hp:
                hp[num] = 1
            else:
                return True

        return False

        
         