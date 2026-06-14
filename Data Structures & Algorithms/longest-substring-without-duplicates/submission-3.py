class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars=set()

        res=0

        l=0
        r=0

        while r<len(s):
            if s[r] not in chars:
                chars.add(s[r])
                res=max(res,len(chars))
                r+=1
            
            else:
                while s[r] in chars:
                    chars.remove(s[l])
                    l+=1
        
        return res
        