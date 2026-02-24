# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def DFS(root,c):
            if not root:
                return 0
            c = ( c * 2 ) + root.val
            if not root.left and not root.right:
                return c
            return DFS(root.left,c) + DFS(root.right,c)
        return DFS(root,0)
