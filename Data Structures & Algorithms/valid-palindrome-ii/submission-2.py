class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1

        skips = 0
        
        def isPalindrome(L,R):
            while L<=R:
                if s[L] != s[R]:
                    return False
                L+=1
                R-=1
            
            return True

        while l<=r:
            if skips >1:
                return False
            if s[l] != s[r]:
                if isPalindrome(l+1,r):
                    skips+=1
                    l+=1
                elif isPalindrome(l,r-1):
                    skips+=1
                    r-=1
                else:
                    return False
            else:
                l+=1
                r-=1
        
        return True
                    