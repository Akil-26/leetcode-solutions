class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def isSelfDividing(num: int) -> bool:
            for d in str(num):
                if d == '0' or num % int(d) != 0:
                    return False
            return True

        return [x for x in range(left, right + 1) if isSelfDividing(x)]
