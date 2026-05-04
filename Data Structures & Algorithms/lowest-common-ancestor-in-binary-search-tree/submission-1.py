# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        crr =root
        while crr:
            if crr.val > p.val and crr.val > q.val:
                crr = crr.left
            elif crr.val < p.val and crr.val < q.val:
                crr= crr.right
            else:
                return crr

        