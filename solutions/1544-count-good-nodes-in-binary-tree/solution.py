# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,val):
            if node is None:
                return 0
            
            good = 0
            
            if node.val >= val:
                good+=1
            
            val = max(node.val,val)
            
            left = dfs(node.left,val)
            right = dfs(node.right,val)
            
            return good + left + right
        
        return dfs(root,root.val)

