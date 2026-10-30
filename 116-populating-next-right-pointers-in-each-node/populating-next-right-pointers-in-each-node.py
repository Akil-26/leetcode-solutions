"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = deque([root])
        while q:
            row = []
            for _ in range(len(q)):
                val = q.popleft()
                if val.left:
                    q.append(val.left)
                if val.right:
                    q.append(val.right)
                row.append(val)
            for i in range(len(row)-1):
                row[i].next = row[i+1]
        return root