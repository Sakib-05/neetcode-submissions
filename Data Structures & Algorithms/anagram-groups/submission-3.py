class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        print(sorted(""))
        ans = []
        seen = set()

        i=0
        while i < len(strs):
            if strs[i] in seen:
                i+=1
                continue
            
            temp = [strs[i]]
            j = i+1
            while j< len(strs):
                if strs[i] == strs[j]:
                    temp.append(strs[j])
                    j+=1
                    continue
                elif sorted(strs[i]) == sorted(strs[j]) and strs[j] not in seen:
                    temp.append(strs[j])
                    seen.add(strs[j]) 
                else:
                    j+=1

            seen.add(strs[i])       
            
            ans.append(temp)
            i+=1

        
        return ans
