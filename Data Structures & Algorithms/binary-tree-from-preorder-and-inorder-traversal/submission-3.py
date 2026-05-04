# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        d= {}
        for i,val in enumerate(inorder):
            d[val] = i
        
        self.ind = 0

        def build(left,right):
            if left > right:
                return None
            val = preorder[self.ind]
            node = TreeNode(val)
            self.ind+=1
            node.left = build(left,d[val]-1)
            node.right = build(d[val]+1,right)
            return node
        
        return build(0,len(preorder)-1)
        
