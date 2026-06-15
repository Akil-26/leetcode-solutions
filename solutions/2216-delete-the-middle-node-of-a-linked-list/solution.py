# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head or not head.next:
        #     return None
        # rang =  0
        # curr = head
        # while curr:
        #     curr = curr.next
        #     rang += 1
        # mid = rang // 2
        # curr = head
        # for _ in range(mid-1):
        #     curr = curr.next
        # curr.next = curr.next.next
        # return head
        if not head or not head.next:
            return None
        curr = fast = slow = head
        while fast and fast.next:
            curr = slow
            slow = slow.next
            fast = fast.next.next
        curr.next = slow.next
        return head
