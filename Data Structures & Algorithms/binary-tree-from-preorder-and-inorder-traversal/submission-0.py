# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d={}
        for i,v in enumerate(inorder):
            d[v]=i
        ind=0
        def build(left,right):
            
            nonlocal ind
            if left>right:
                return None
            val = preorder[ind]
            root = TreeNode(val)
            ind+=1
            root.left= build(left,d[val]-1)
            root.right= build(d[val]+1,right)
            return root




        return build(0,len(preorder)-1)