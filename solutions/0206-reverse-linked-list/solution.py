# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        value = []
        while curr:
            value.append(curr.val)
            curr = curr.next
        value = value[::-1]
        cur = head
        i = 0
        while i < len(value):
            cur.val = value[i]
            cur = cur.next
            i+=1
        return head
