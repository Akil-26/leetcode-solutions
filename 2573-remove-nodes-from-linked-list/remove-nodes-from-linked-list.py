# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        head = reverse(head)
        curr = head
        while curr and curr.next:
            if curr.next.val < curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return reverse(head)