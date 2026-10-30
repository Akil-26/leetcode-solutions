# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:

        if not root:
            return []
        swap = 1
        q = deque([root])
        res = []
        while q:
            row = []
            for _ in range(len(q)):
                v = q.popleft()
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
                row.append(v.val)
            
            if swap:
                res.append(row)
                swap = 0
            else:
                res.append(row[::-1])
                swap = 1
        return res