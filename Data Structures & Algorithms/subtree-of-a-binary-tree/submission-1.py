# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return check(p.left,q.left) and check(p.right,q.right)
        self.flag = False
        q = [root]
        while q:
            node = q.pop(0)
            if node.val == subRoot.val and check(node,subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False

        
