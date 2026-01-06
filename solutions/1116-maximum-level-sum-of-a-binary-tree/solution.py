from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        min_l = float('-inf')
        ans_l = 1
        level = 1
        while q:
            size = len(q)
            level_sum = 0
            for _ in range (size):
                cur= q.popleft()
                level_sum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if level_sum > min_l:
                min_l = level_sum
                ans_l = level
            level += 1
        return ans_l
