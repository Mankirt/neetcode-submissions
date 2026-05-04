# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        crr = root
        temp_stack = []
        while crr or temp_stack:
            while crr:
                temp_stack.append(crr)
                crr = crr.left
            last = temp_stack.pop()
            st.append(last.val)
            if last.right:
                crr = last.right
        
        return st