class Solution:
    def intToRoman(self, num: int) -> str:
        ro = ""
        st = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        for i in range(len(st)):
            while num >= st[i][0]:
                ro += st[i][1]
                num -= st[i][0]
        return ro
