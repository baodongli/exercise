class Solution:
    def totalNQueens(self, n: int) -> int:
        queenPos = [-1 for _ in range(n)]
        all_cols = [0 for _ in range(n)]
        totals = 0
        def noDiagnalCollision(row, col, queenPos):
            for qr, qc in enumerate(queenPos[:row]):
                if abs(row-qr) == abs(col-qc ):
                    return False
            return True
        def placeQueenOnRow(row, queenPos, all_cols):
            nonlocal totals
            if row == n:
                totals += 1
                return
            for col in range(n):
                if all_cols[col] == 0 and noDiagnalCollision(row, col, queenPos):
                    queenPos[row] = col
                    all_cols[col] = 1
                    placeQueenOnRow(row + 1, queenPos, all_cols)
                    all_cols[col] = 0
        placeQueenOnRow(0, queenPos, all_cols)
        return totals
