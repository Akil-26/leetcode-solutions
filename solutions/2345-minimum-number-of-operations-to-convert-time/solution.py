class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def take_time(t):
            h,m = map(int,t.split(":"))
            return h * 60 + m 
        
        cur = take_time(current)
        cor = take_time(correct)

        dif = cor - cur
        op = 0

        for step in [60,15,5,1]:
            op += dif//step
            dif %= step
        return op
