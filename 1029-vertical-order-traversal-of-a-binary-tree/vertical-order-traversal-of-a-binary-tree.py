# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return root
        d = defaultdict(list)
        q = deque([(root,0)])
        while q:
            d1 = defaultdict(list)
            for _ in range(len(q)):
                val,idx = q.popleft()
                d1[idx].append(val.val)
                if val.left:
                    q.append((val.left,idx-1))
                if val.right:
                    q.append((val.right,idx+1))
            for i,j in d1.items():
                j.sort()
                d[i].extend(j)
        mi = min(d.keys())
        ma = max(d.keys())
        res = []
        for i in range(mi,ma+1):
            res.append(d[i])
        return res
            