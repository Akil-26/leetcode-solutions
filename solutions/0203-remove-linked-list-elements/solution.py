# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur1 = ListNode(0)
        cur1.next = head
        cur2 = cur1
        while cur2.next:
            if cur2.next.val == val:
                cur2.next = cur2.next.next
            else:
                cur2 = cur2.next
        return cur1.next
        """
        cur = head
        while cur:
            if cur.val == val:
                cur.val = None
                head = cur.next
            elif cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next
        return head
        """
