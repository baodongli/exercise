class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        #taken = [[0 for _ in range(n)] for _ in range(m)]

        def findWord(row, col, pos, word):
            if pos == len(word):
                return True
            if row < 0 or row >= m or col < 0 or col >= n:
                return False
            if board[row][col] == '':
                return False
            saved_letter = ''
            if board[row][col] == word[pos]:
                saved_letter = word[pos]
                board[row][col] = ''
                #taken[row][col] = 1
            else:
                return False
            if findWord(row, col+1, pos+1, word):
                return True
            if findWord(row, col-1, pos+1, word):
                return True
            if findWord(row+1, col, pos+1, word):
                return True
            if findWord(row-1, col, pos+1, word):
                return True
            #taken[row][col] = 0
            board[row][col] = saved_letter
            return False

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if findWord(r, c, 0, word):
                        return True
        return False
