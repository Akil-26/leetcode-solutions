class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f_r = set("qwertyuiop")
        s_r = set("asdfghjkl")
        t_r = set("zxcvbnm")
        res = []
        for w in words:
            wa = set(w.lower())
            if wa <= f_r or wa <= s_r or wa <= t_r:
                res.append(w)
        return res
