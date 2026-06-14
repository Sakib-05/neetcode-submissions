class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res =0

        stack = []

        for token in tokens:
            if token in "+-*/":
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if token == "+":
                    plus = op1 + op2
                    stack.append(plus)
                    print(stack)
                elif token == "-":
                    sub = op1 - op2
                    stack.append(sub)
                    print(stack)
                elif token == "*":
                    mul = op1 * op2
                    stack.append(mul)
                    print(stack)
                
                elif token == "/":
                    div = int(op1/op2)
                    stack.append(div)
                    
                    print(stack)
            else:
                stack.append(int(token))
                print(stack)
            
        res = stack[-1]

        return res



        