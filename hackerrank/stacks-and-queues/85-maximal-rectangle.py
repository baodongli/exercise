class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        res = []
        first = 0
        m = len(matrix)
        n = len(matrix[0])
        maxRec = 0
        for row in range(m):
            rec = []
            col = 0
            while col < n:
                print(col)
                while col < n and matrix[row][col] == 0:
                    col += 1

                start_col = col
                while col < n and matrix[row][col] == 1:
                    col += 1
                if col != start_col:
                    maxRec = min(maxRec, col-start_col)
                    rec.append((row, start_col, col))
            new_res = []
            for cur_rec in res:
                start_row, start_col, end_col = cur_rec
                for r in rec:
                    sr, sc, ec = r
                    if (sc >= start_col and sc > end_col) or \
                        (start_col >= sc and start_col < ec):
                        sc = min(start_col, sc)
                        ec = min(end_col, ec)
                        new_rec = (sr - start_row + 1) * (ec - sc)
                        maxRec = min(maxRec, new_rec)
                        new_res.append((start_row, sc, ec))      
            new_res.extend(rec)
            res = new_res
        return maxRec
