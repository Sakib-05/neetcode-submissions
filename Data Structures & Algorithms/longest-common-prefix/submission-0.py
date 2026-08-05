class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        res = ""
        for string in strs:
            if len(string) > len(longest): longest = string
        
        error = False
        for i,e in enumerate(longest):
            for word in strs:
                if i >= len(word) or word[i] !=e:
                    error = True
                    break
            
            if error:
                break
            res += e
            
                
        return res
        