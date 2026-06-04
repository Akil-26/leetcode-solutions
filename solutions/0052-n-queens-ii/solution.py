class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.']*n for i in range(n)]
        col = set()
        pos = set()
        neg = set()
        sol = []
        def bt(r):
            if r == n:
                sol.append([''.join(row) for row in board])
            for c in range(n):
                if c in col or r+c in pos or r-c in neg:
                    continue
                board[r][c] = 'Q'
                col.add(c)
                pos.add(r+c)
                neg.add(r-c)

                bt(r+1)

                board[r][c] = '.'
                col.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
        bt(0)
        return len(sol)
