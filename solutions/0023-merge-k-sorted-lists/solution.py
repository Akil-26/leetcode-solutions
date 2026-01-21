# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        res = []
        for i in lists:
            curr = i
            while curr:
                res.append(curr.val)
                curr = curr.next
        res.sort()
        cur = dummy
        for i in res:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next
