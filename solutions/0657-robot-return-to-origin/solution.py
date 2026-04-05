class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ver = hor = 0 
        for step in moves:
            if step == "U":
                ver += 1
            elif step == "D":
                ver -= 1
            elif step == "L":
                hor += 1
            elif step == "R":
                hor -= 1
        return ver == 0 and hor == 0
