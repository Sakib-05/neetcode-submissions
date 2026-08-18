class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hp ={}

        for i,e in enumerate(nums):
            if e not in hp: 
                hp[e] = i
                continue
            
            if e in hp and abs(hp[e] - i) <=k:
                return True
            
            hp[e] = i
        
        return False

            
        