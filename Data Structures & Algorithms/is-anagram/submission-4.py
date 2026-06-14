class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sp = [0] *26
        print(sp)

        for char in s:
            sp[ord(char)-97] +=1

        tp = [0]*26

        for char in t:
            tp[ord(char)-97]+=1
        
        if sp != tp:
            return False

        return True
        