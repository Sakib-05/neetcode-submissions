class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        res=0
        l=0
        
        r=0

        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                res=max(res,r-l+1)
                r+=1
            else:
                l+=1
                r=l
                chars=set()

        return res
        