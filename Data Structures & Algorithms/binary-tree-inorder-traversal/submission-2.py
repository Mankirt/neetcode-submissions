# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode], ans =[]) -> List[int]:
        stack = []
        crr = root
        ans = []
        while crr or stack:
            while crr:
                stack.append(crr)
                crr = crr.left
            crr = stack.pop()
            ans.append(crr.val)
            crr = crr.right
        return ans
            