class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        head = head.next
        start = head
        while start:
            end = start  
            sum = 0
            while end.val != 0:
                sum += end.val
                end = end.next
            start.val = sum  
            start.next = end.next  
            start = start.next 
        return head
