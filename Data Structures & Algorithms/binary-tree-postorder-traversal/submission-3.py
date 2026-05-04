# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        crr = root
        st = [crr]
        visit = [False]
        res = []
        while st:
            node = st.pop()
            v = visit.pop()
            if node:
                if v:
                    res.append(node.val)
                else:
                    st.append(node)
                    visit.append(True)
                    st.append(node.right)
                    visit.append(False)
                    st.append(node.left)
                    visit.append(False)
        
        return res
