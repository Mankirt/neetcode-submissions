# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ma = -1001
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            val = max(node.val,node.val+left+right, node.val+left,node.val+right)
            self.ma = max(self.ma,val)
            return max(node.val, node.val+left,node.val+right)
        dfs(root)
        return self.ma
        
