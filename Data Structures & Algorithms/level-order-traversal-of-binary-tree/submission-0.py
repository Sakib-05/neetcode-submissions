# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def height(node):
            if node is None:
                return 0
            
            left = height(node.left) if node.left else 0
            right = height(node.right) if node.right else 0

            return 1 + max(left, right)

        print(f"height is {height(root)}")

        levels = height(root)

        res = [ [] for level in range(levels)]
        print("res",res)

        que = deque([(root, 0)])

        while que:
            node, level = que.popleft()

            if node is not None: 
                res[level].append(node.val)
                if node.left: que.append((node.left,level+1))
                if node.right: que.append((node.right, level+1))



        return res
        