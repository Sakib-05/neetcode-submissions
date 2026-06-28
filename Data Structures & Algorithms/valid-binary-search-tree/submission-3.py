# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            if node is None:
                return []
            
            res = []

            res.extend(inorder(node.left))
            res.append(node.val)
            res.extend(inorder(node.right))

            return res

        
        print(inorder(root))

        inorderList = inorder(root)
        for i in range(1,len(inorderList)):
            if inorderList[i-1]>= inorderList[i]:
                return False

        return True

        