# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.ind = 0
        s={}
        for i,v in enumerate(inorder):
            s[v]=i
        def build(left,right):
            if left>right:
                return None
            val = preorder[self.ind]
            root = TreeNode(val)
            self.ind+=1
            root.left = build(left,s[val]-1)
            root.right = build(s[val]+1,right)
            return root
        
        return build(0,len(preorder)-1)