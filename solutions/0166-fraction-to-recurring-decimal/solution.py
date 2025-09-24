class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []

        # 1. Handle sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        # Convert to absolute values for calculation
        numerator = abs(numerator)
        denominator = abs(denominator)

        # 2. Integer part
        res.append(str(numerator // denominator))

        remainder = numerator % denominator
        if remainder == 0:
            return "".join(res)
        res.append(".")
        remainder_map = {} 
        while remainder != 0:
            if remainder in remainder_map:
                insert_pos = remainder_map[remainder]
                res.insert(insert_pos, "(")
                res.append(")")
                return "".join(res)
            remainder_map[remainder] = len(res) 
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator
        return "".join(res)
