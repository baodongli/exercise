class Solution:
    '''
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        queenPos = [-1 for _ in range(n)]
        def noCollision(row, col):
            for qr in range(row):
                qc = queenPos[qr]
                if col == qc:
                    return False
                if abs(row - qr) == abs(col - qc):
                    return False
            return True
        def placeQueueOnRow(row):
            nonlocal queenPos, ans
            if row == n:
                res = []
                for qr, qc in enumerate(queenPos):
                    row_res = ['.' for _ in range(n)]
                    row_res[qc] = 'Q'
                    res.append(''.join(row_res))
                ans.append(res)
                return

            for col in range(n):
                if noCollision(row, col):
                    queenPos[row] = col
                    placeQueueOnRow(row+1)
        placeQueueOnRow(0)
        return ans
    '''
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        all_cols = [-1 for i in range(n)]
        ans = []
        queenPos = [-1 for _ in range(n)]
        board = [['.' for i in range(n)] for _ in range(n)]
        def noDiagnalCollision(row, col):
            for qr in range(row):
                qc = queenPos[qr]
                #if col == qc:
                #    return False
                if abs(row - qr) == abs(col - qc):
                    return False
            return True
        def placeQueueOnRow(row, occupied_cols):
            nonlocal queenPos, ans
            if row == n:
                res = []
                for qr, qc in enumerate(queenPos):
                    board[qr][qc] = 'Q'
                for qr, qc in enumerate(queenPos):
                    res.append(''.join(board[qr]))
                    board[qr][qc] = '.'
                ans.append(res)
                return

            for col, v in enumerate(occupied_cols):
                if v == -1 and noDiagnalCollision(row, col):
                    queenPos[row] = col
                    occupied_cols[col] = col
                    placeQueueOnRow(row+1, occupied_cols)
                    occupied_cols[col] = -1
        placeQueueOnRow(0, all_cols)
        return ans
