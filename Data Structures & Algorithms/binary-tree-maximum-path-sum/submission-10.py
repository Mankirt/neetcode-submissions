# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [-1001]
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            left = 0 if left<0 else left
            right = 0 if right<0 else right
            res[0] = max(res[0], left + right + node.val)

            return node.val + max(left,right)
        
        dfs(root)
        return res[0]
