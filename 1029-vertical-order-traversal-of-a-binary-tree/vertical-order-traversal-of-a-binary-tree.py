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
        
        q = deque([(root,0)])
        dic = defaultdict(list)

        while q:
            dic1 = defaultdict(list)
            for _ in range(len(q)):
                val,idx = q.popleft()
                dic1[idx].append(val.val)
                if val.left:
                    q.append((val.left,idx-1))
                if val.right:
                    q.append((val.right,idx+1))
            for i,j in dic1.items():
                j.sort()
                dic[i] += j
        mi = min(dic.keys())
        ma = max(dic.keys())
        res = []

        for i in range(mi,ma+1):
            res.append(dic[i])
        
        return res