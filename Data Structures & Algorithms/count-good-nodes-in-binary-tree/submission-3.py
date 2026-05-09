# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root,root.val)]) #node, node.val
        ans = 1
        while q:
            node, mx_val = q.popleft()
            if node.left:
                if node.left.val >= mx_val:
                    ans += 1
                q.append((node.left,max(mx_val, node.left.val)))
            if node.right:
                if node.right.val >= mx_val:
                    ans += 1
                q.append((node.right,max(mx_val, node.right.val)))
        
        return ans