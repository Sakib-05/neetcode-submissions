class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        hp={}

        l,r=0,0

        while r< len(s):
            hp[s[r]] = hp.get(s[r],0)+1

            maxfrequency = max(hp.values())

            if r-l +1 - max(hp.values()) <= k:
                res = max(r-l+1,res)
            
            else:
                while r-l +1 - max(hp.values()) > k:
                    hp[s[l]] -=1
                    l+=1
            
            r+=1
        

        return res

        