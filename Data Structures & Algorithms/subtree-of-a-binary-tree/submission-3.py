# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(sub, main):
            if not sub and not main:
                return True
            if not sub or not main or sub.val != main.val:
                return False
            return check(sub.left,main.left) and check(sub.right, main.right)

        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                if check(subRoot,node): return True
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False
            