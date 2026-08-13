class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if len(stack)==0: stack.append(ast)

            else:
                top = stack[-1]

                # same direction: both right or both left or (<- and ->)
                if (top>0 and ast>0) or (top<0 and ast<0) or (top<0 and ast>0):
                    stack.append(ast)

                # opposite directions: -> and <-
                else:
                    ast_broken= False
                    while stack and stack[-1] >0:
                        if abs(stack[-1]) == abs(ast): 
                            ast_broken = True
                            stack.pop()
                            break
                        # top is bigger
                        elif abs(stack[-1]) > abs(ast):
                            ast_broken = True
                            break
                        # top is smaller
                        else:
                            stack.pop()

                    if not ast_broken:
                        stack.append(ast)

        
        return stack



        