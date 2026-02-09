# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        val = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            val.append(root.val)
            inorder(root.right)

        inorder(root)

        def balanced_tree(nums):
            if not nums:
                return
            mid = len(nums) // 2
            root = TreeNode(nums[mid])

            root.left = balanced_tree(nums[:mid])
            root.right = balanced_tree(nums[mid+1:])

            return root
        return balanced_tree(val)
