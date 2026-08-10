class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hp = {0:0,1:0,2:0}

        for num in nums:
            hp[num] +=1

        for i in range(hp[0]):
            nums[i] = 0
        
        for i in range(hp[0],hp[0]+hp[1]):
            nums[i] = 1
        
        for i in range(hp[0]+hp[1],hp[0]+hp[1]+hp[2]):
            nums[i] =2
        
        print(nums)
        