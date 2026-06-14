class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s)
        i=0
        j= len(s) -1
        numbers= {'1','2','3','4','5','6','7','8','9','0'}
        while i<=j and len(s) !=0:
            while (ord(s[i].lower()) -96 < 1 or ord(s[i].lower()) -96 > 26) and i<j :
                if s[i] in numbers:
                    break
                i+=1
            while (ord(s[j].lower()) -96 < 1 or ord(s[j].lower()) -96 > 26) and i<j:
                if s[j] in numbers:
                    break
                j-=1
            
            if s[i].lower() != s[j].lower():
                return False
            
            else:
                i+=1
                j-=1
            

        return True
        