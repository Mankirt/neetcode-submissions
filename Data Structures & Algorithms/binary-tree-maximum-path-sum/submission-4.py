# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=-1001
        def dfs(node):
            if node==None:
                return 0
            nonlocal ans
            val = node.val
            left = dfs(node.left)
            right = dfs(node.right)
            if left > 0:
                val += left
            if right > 0:
                val += right
            ans = max(val, ans)
            return max(node.val +left, node.val + right, node.val)
        dfs(root)
        return ans
