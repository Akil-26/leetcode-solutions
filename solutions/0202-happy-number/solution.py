class Solution:
    def isHappy(self, n: int) -> bool:
        
        def next_num(num):
            return sum(int(d)**2 for d in str(num))

        slow = n
        fast = next_num(n)

        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))

        return fast == 1
