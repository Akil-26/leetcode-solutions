class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
        # under this code gives extra space because u will change int and string
        """res = ''
        for i in digits:
            res += str(i)
        return list(int(i) for i in str(int(res)+1))"""
