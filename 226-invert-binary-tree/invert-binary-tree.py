# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ## using stack
        if not root:
            return None
        stack = [root]
        while stack:
            parent = stack.pop()
            parent.left ,parent.right = parent.right , parent.left
            if parent.left:
                stack.append(parent.left)
            if parent.right:
                stack.append(parent.right)
        return root