# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        li = []
        while cur:
            li.append(cur.val)
            cur = cur.next
        li.sort()
        cur = head
        for i in li:
            cur.val = i
            cur = cur.next
        return head

