class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hp = defaultdict(list)

        for string in strs:
            pattern = [0] *26

            for char in string:
                pattern[ord(char)-97]+=1
            
            hp[tuple(pattern)].append(string)
        

        # print(hp)
        # res=[]
        # for key in hp:
        #     res.append(hp[key])



        return list(hp.values())

        