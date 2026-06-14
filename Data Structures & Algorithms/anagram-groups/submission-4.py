class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            charFrequency = [0] *26
            for char in string:
                charFrequency[ord(char)- ord("a")] +=1
            
            
            res[tuple(charFrequency)].append(string)
            
        ans = list(res.values())

        return ans