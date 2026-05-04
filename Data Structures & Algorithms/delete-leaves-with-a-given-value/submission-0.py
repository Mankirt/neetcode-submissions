# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        dummy = TreeNode(left = root)

        q = [(root,dummy,1)]
        temp = deque([(root,dummy,1)])
        while temp:
            node, par, l = temp.popleft()
            if node.left:
                temp.append((node.left,node,1))
                q.append((node.left,node,1))
            if node.right:
                temp.append((node.right,node,0))
                q.append((node.right,node,0))
        
        while q:
            node, par, l = q.pop()
            if not node.left and not node.right and node.val == target:
                if l:
                    par.left = None
                else:
                    par.right = None
        return dummy.left
            
