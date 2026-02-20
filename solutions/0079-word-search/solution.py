class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def DFS(i,j,ind):
            if ind == len(word):
                return True

            if not (0<=i<row and 0<=j<col) or board[i][j] != word[ind]:
                return False
                
            temp = board[i][j]
            board[i][j] = '#'
            found = (
                     DFS(i+1,j,ind+1) or 
                     DFS(i-1,j,ind+1) or 
                     DFS(i,j+1,ind+1) or 
                     DFS(i,j-1,ind+1)
                    )
            board[i][j] = temp
            return found
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if DFS(i,j,0):
                        return True
        return False
