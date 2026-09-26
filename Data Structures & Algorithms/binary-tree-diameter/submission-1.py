# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if node is None:
                return 0
            
            return 1+ max(height(node.left) ,height(node.right))

        res = 0

        que = deque([root])

        while que:
            node = que.popleft()
            left = height(node.left)
            right = height(node.right)

            res = max(left+right, res)

            if node.left: que.append(node.left)
            if node.right: que.append(node.right)



        


        return res




        