from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        q = deque([root])
        values = []
        while q:
            row = []
            for _ in range(len(q)):
                val = q.popleft()
                row.append(val.val)
                if val.left:
                    q.append(val.left)
                if val.right:
                    q.append(val.right)
            values.append(row)
        return row[0]