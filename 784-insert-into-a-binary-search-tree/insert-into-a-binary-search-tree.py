# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        def insert(root,val):
            if val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                return insert(root.left,val)
            elif val > root.val:
                if not root.right:
                    root.right = TreeNode(val)
                return insert(root.right,val)
        if not root and val:
            root = TreeNode(val)
            return root
        insert(root,val)
        return root