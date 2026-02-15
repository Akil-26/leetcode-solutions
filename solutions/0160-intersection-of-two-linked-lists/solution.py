# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setA = set()
        currA = headA
        while currA:
            setA.add(currA)
            currA = currA.next
        
        setB = set()
        currB = headB
        while currB:
            if currB in setA:
                return currB
            currB = currB.next

        return None
