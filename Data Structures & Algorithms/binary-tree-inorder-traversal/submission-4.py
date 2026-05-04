# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def ino(node):
            if not node:
                return
            ino(node.left)
            ans.append(node.val)
            ino(node.right)
        
        ino(root)
        return ans