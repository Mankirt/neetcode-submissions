# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(root,check):
            if not root and not check:
                return True
            if not root or not check or root.val!=check.val:
                return False
            
            return (same(root.left,check.left) and same(root.right,check.right))
        
        q=[root]
        while q:
            node=q.pop(0)
            if node.val==subRoot.val and same(node,subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False