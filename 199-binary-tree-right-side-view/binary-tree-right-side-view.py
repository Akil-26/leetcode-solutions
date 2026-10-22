from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        q = deque([root])
        values = []
        while q:
            row = []
            for _ in range(len(q)):
                v = q.popleft()
                row.append(v.val)
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
            values.append(row[-1])
        return values