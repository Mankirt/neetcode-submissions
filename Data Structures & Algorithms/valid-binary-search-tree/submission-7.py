# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, mx , mn):
            if not node:
                return True
            if not mn < node.val < mx: return False
            return check(node.left, node.val, mn) and check(node.right, mx, node.val)
        
        return check(root, float('inf'), float('-inf'))