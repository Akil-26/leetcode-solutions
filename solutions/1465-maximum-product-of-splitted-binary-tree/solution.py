# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root):
        MOD = 1000000007
        self.max_product = 0
        # STEP 1: Find total sum of tree
        def find_total_sum(node):
            if node is None:
                return 0
            left_sum = find_total_sum(node.left)
            right_sum = find_total_sum(node.right)
            return node.val + left_sum + right_sum
        total_sum = find_total_sum(root)
        # STEP 2: Try splitting at every subtree
        def find_subtree_sum(node):
            if node is None:
                return 0
            left = find_subtree_sum(node.left)
            right = find_subtree_sum(node.right)
            subtree_sum = node.val + left + right
            product = subtree_sum * (total_sum - subtree_sum)
            if product > self.max_product:
                self.max_product = product
            return subtree_sum
        find_subtree_sum(root)
        return self.max_product % MOD
