class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()

        res = 0

        l=0
        n= len(s)
        for r in range(n):
            if s[r] not in st:
                st.add(s[r])
                res = max(res, r-l+1)
            
            else:
                while s[r] in st:
                    st.discard(s[l])
                    l+=1
                st.add(s[r])
        
        return res
        