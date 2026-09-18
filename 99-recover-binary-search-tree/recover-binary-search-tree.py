# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = second = prev = None
        cur = root
        while cur:
            if not cur.left:
                if prev and prev.val > cur.val:
                    if not first:
                        first = prev
                    second = cur
                prev = cur
                cur = cur.right
            else:
                temp = cur.left
                while temp.right and temp.right != cur:
                    temp = temp.right
                if not temp.right:
                    temp.right = cur
                    cur = cur.left
                else:
                    temp.right = None
                    if prev and prev.val > cur.val:
                        if not first:
                            first = prev
                        second = cur
                    prev = cur
                    cur = cur.right
        if first and second :
            first.val,second.val = second.val,first.val