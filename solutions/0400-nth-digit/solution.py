class Solution:
    def findNthDigit(self, n: int) -> int:
        """dt = 1
        st = 1
        co = 9
        while n > dt * co:
            n -= dt * co
            dt += 1
            co *= 10
            st *= 10
        num = st + (n-1) // dt
        return int(str(num)[(n-1)%dt])"""
        ranges = [
            (1, 1, 9),
            (2, 10, 90),
            (3, 100, 900),
            (4, 1000, 9000),
            (5, 10000, 90000),
            (6, 100000, 900000),
            (7, 1000000, 9000000),
            (8, 10000000, 90000000),
            (9, 100000000, 900000000),
        ]
        for dt ,st , co in ranges:
            if n > dt * co:
                n -= dt * co
            else:
                num = st + (n-1) // dt
                return int(str(num)[(n-1)%dt])
