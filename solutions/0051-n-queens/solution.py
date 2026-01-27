class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def is_safe(board,col,row):
            i = col 
            while i >= 0:
                if board[row][i] == "Q":
                    return False
                i-=1
            i ,j = col,row
            while i >= 0 and j >= 0:
                if board[j][i] == "Q":
                    return False
                i-=1
                j-=1
            i ,j = col,row
            while i >= 0 and j < n:
                if board[j][i] == "Q":
                    return False
                i-=1
                j+=1
            return True
        def solution(board,col):
            if col == n:
                res.append(["".join(r) for r in board])
                return
            for row in range(n):
                if is_safe(board,col,row):
                    board[row][col] = "Q"
                    solution(board,col+1)
                    board[row][col] = "."
        board = [["."]*n for i in range(n)]
        solution(board,0)
        return res
