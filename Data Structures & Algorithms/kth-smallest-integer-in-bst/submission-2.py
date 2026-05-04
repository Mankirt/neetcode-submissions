# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        crr = root
        while k > 0:
            while crr:
                st.append(crr)
                crr=crr.left
            node = st.pop()
            last = node.val
            k-=1
            if node.right:
                crr = node.right
        
        return last