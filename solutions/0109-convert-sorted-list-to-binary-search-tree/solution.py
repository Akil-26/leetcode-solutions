# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        def find(curr):
            if curr:
                nums.append(curr.val)
                find(curr.next)
            else:
                return
        find(head)
        def balanced(nums):
            if not nums:
                return 
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = balanced(nums[:mid])
            root.right = balanced(nums[mid+1:])

            return root
        return balanced(nums)
