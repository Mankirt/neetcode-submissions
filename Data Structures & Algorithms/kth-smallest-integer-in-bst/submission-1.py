# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        crr = root
        stack = []
        n = 0
        while crr or stack:
            while crr:
                stack.append(crr)
                crr=crr.left
            crr = stack.pop()
            n+=1
            if n==k:
                return crr.val
            crr = crr.right