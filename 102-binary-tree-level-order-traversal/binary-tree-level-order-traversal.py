from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            lev = []
            for i in range(len(q)):
                val = q.popleft()
                lev.append(val.val)
                if val.left:
                    q.append(val.left)
                if val.right:
                    q.append(val.right)
            res.append(lev)
        return res