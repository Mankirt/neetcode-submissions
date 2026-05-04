# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        l = []
        def dfs(node):
            if not node:
                l.append("N")
                return
            l.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print(l)
        return ".".join(l)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        l = data.split(".")
        self.ind = 0
        def dfs():
            if self.ind==len(l):
                return None
            if l[self.ind] == 'N':
                self.ind+=1
                return None
            root = TreeNode(int(l[self.ind]))
            self.ind+=1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
                