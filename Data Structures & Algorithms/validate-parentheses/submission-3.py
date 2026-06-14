class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bopen = "({["
        hp = {'(':')', '{':'}', '[':']'}


        #go thorugh every charcter in s
        #if its an open add it to the stack
        #if its a closing bracket then chek at the top of the stack and if its correct type of
        #the open bracket on top then pop and continue
        #else return false 


        for char in s:
            if char in bopen:
                stack.append(char)
            elif len(stack) >0:
                if hp[stack.pop()] != char:
                    return False
            else:
                return False
        
        if len(stack) >0:
            return False




        return True




        