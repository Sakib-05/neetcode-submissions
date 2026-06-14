class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        if len(strs)==0:
            return "none"
        string = ""
        for x in range(len(strs)-1):
            string += strs[x] + "~~"
        
        string+= strs.pop()

        return string

    def decode(self, s: str) -> List[str]:
        if s== "":
            return [""]
        if s == "none":
            return []
        return s.split("~~")
