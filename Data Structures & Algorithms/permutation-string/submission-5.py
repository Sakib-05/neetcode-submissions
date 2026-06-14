class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = defaultdict(int)

        for char in s1:
            s1map[char] +=1
        
        window_size = len(s1)


        
        
        l,r=0,window_size-1

        while r<len(s2):
            tempmap = defaultdict(int)
            substring = s2[l:r+1]
            for char in substring:
                tempmap[char] +=1
            
            if tempmap ==s1map:
                return True
            
            l+=1
            r+=1

        





        return False
        