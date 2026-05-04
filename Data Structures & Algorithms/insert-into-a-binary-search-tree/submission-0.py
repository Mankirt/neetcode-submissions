# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        crr = root
        while True:
            if crr.val > val:
                if not crr.left:
                    crr.left = TreeNode(val)
                    return root
                crr= crr.left
            else:
                if not crr.right:
                    crr.right = TreeNode(val)
                    return root
                crr= crr.right