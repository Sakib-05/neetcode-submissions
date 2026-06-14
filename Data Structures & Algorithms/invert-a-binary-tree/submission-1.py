# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        que = []
        if root: que.append(root)

        while que:
            node=que.pop()
            node.left,node.right = node.right, node.left
            if node.left: que.append(node.left)
            if node.right : que.append(node.right)
        




        return root
        