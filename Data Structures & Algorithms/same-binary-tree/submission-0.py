# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_que = [p]
        q_que = [q]

        while p_que and q_que:
            p_node = p_que.pop()
            q_node = q_que.pop()

            if (p_node is not None and q_node is None) or (q_node is not None and p_node is None):
                return False

            if (p_node and q_node) and p_node.val != q_node.val:
                return False
            
            if p_node is not None:
                p_que.append(p_node.left)
                p_que.append(p_node.right)
            if q_node is not None:
                q_que.append(q_node.left)
                q_que.append(q_node.right)
        
        if p_que or q_que:
            return False

        return True


            


        