class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        res = []

        for i in range(min(n,m)):
            res.append(word1[i])
            res.append(word2[i])
        
        if i<n or i<m:
            if n<m:
                res.append(word2[i+1:m])
            else:
                res.append(word1[i+1:n])
            
        return "".join(res)

        