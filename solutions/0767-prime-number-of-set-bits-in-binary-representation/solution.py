class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        co = 0
        def isprime(n):
            if n <= 1:
                return False
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
        for i in range(left,right+1):
            count = bin(i).count("1")
            if isprime(count):
                co+=1
        return co
