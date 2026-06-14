# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def treeH(node):
            if node:
                left = treeH(node.left) if node.left else 0
                right = treeH(node.right) if node.right else 0
        
                return 1+ max(left,right)
            
            else:
                return 0

        res=True
        que=deque([root])
        while que:
            tnode=que.popleft()
            if tnode:
                if tnode.left: que.append(tnode.left)
                if tnode.right: que.append(tnode.right)
                left=treeH(tnode.left)
                right=treeH(tnode.right)

                if abs(left - right) >1:
                    res = False
        
        return res



        