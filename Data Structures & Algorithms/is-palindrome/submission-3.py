class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        print(s)
        s= "".join(s.split(" "))
        i=0
        j= len(s) -1
        numbers= {'1','2','3','4','5','6','7','8','9','0'}
        while i<=j and len(s) !=0:
            while (ord(s[i]) -96 < 1 or ord(s[i]) -96 > 26) and i<j :
                if s[i] in numbers:
                    break
                i+=1
            while (ord(s[j]) -96 < 1 or ord(s[j]) -96 > 26) and i<j:
                if s[j] in numbers:
                    break
                j-=1
            
            if s[i] != s[j]:
                return False
            
            else:
                i+=1
                j-=1
            

        return True
        