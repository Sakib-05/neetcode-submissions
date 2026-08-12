class Solution:
    def calPoints(self, operations: List[str]) -> int:
        signs = {"D", "+", "C"}

        stack = []

        for op in operations:
            if op not in signs:
                stack.append(int(op))
            
            elif op == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                addition = n1+n2
                stack.append(n2)
                stack.append(n1)
                stack.append(addition)
            
            elif op == "D":
                double = stack[-1] * 2
                stack.append(double)
            
            else:
                stack.pop()
        
        return sum(stack)




            

        