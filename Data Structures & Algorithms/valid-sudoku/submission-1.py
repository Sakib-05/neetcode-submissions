class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check every row
        #check every column
        #check every 3x3 box
        for row in board:
            seen= set()
            for element in row:
                if element == ".":
                    continue
                elif element in seen:
                    return False
                else:
                    seen.add(element)
        
        for i in range(9):
            seen= set()
            for j in range(9):
                if board[j][i] ==".":
                    continue
                elif board[j][i] in seen:
                    return False
                else:
                    seen.add(board[j][i])
        
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                seen= set()

                a,b,c= board[i][j], board[i][j+1], board[i][j+2]
                d,e,f= board[i+1][j], board[i+1][j+1], board[i+1][j+2]
                g,h,x = board[i+2][j], board[i+2][j+1], board[i+2][j+2]
                if a !=".":
                    seen.add(a)
                
                if b in seen and b != ".":
                    return False
                seen.add(b)
                if c  in seen and c !=".":
                    return False
                seen.add(c)
                if d in seen and d !=".":
                    return False
                seen.add(d)
                if e in seen and e !=".":
                    return False
                seen.add(e)
                if f in seen and f !=".":
                    return False
                seen.add(f)
                if g in seen and g !=".":
                    return False
                seen.add(g)
                if h in seen and h !=".":
                    return False
                seen.add(h)
                if x in seen and x !=".":
                    return False
                seen.add(x)
                
        
        return True

            







        