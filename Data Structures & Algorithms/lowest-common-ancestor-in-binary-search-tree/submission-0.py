# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        visited_nodes_p = []

        node = root

        while True:
            if node and p:
                visited_nodes_p.append(node.val)
                if node.val == p.val:
                    break
                if p.val < node.val:
                    node = node.left
                
                else:
                    node = node.right
        
        visited_nodes_q = []

        node = root

        while True:
            if node and q:
                visited_nodes_q.append(node.val)

                if node.val == q.val:
                    break
                if q.val < node.val:
                    node = node.left
                
                else:
                    node = node.right
            else:
                break
        
        print(str(visited_nodes_p))
        print(str(visited_nodes_q))

        n = min(len(visited_nodes_p), len(visited_nodes_q))

        res = root.val

        for i in range(n):
            if visited_nodes_p[i] == visited_nodes_q[i]:
                res = visited_nodes_p[i]
            else:
                break


        return TreeNode(res)

        