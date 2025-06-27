class Solution:
    '''
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
                while col < n and matrix[row][col] == '0':
                    col += 1

                start_col = col
                while col < n and matrix[row][col] == '1':
                    col += 1
                if col != start_col:
                    maxRec = max(maxRec, col-start_col)
                    rec.append((row, start_col, col))
            new_res = []
            for cur_rec in res:
                start_row, start_col, end_col = cur_rec
                for r in rec:
                    sr, sc, ec = r
                    if (sc >= start_col and sc < end_col) or \
                        (start_col >= sc and start_col < ec):
                        sc = max(start_col, sc)
                        ec = min(end_col, ec)
                        new_rec = (sr - start_row + 1) * (ec - sc)
                        maxRec = max(maxRec, new_rec)
                        new_res.append((start_row, sc, ec))      
            new_res.extend(rec)
            res = new_res
            print(res)
        return maxRec
    '''
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        maxRec = 0
        def findMaxRec(row, res, matrix):
            nonlocal maxRec
            if row == m:
                return
            rec = []
            col = 0
            while col < n:
                while col < n and matrix[row][col] == '0':
                    col += 1

                start_col = col
                while col < n and matrix[row][col] == '1':
                    col += 1
                if col != start_col:
                    maxRec = max(maxRec, col-start_col)
                    rec.append((row, start_col, col))
            new_res = []
            for r in rec:
                sr, sc, ec = r
                used = False
                need_to_add = False
                for cur_rec in res:
                    start_row, start_col, end_col = cur_rec
                    if (sc >= start_col and sc < end_col) or \
                        (start_col >= sc and start_col < ec):
                        new_sc = max(start_col, sc)
                        new_ec = min(end_col, ec)
                        new_rec = (sr - start_row + 1) * (new_ec - new_sc)
                        maxRec = max(maxRec, new_rec)
                        new_res.append((start_row, new_sc, new_ec))      
                        used = True
                        if (new_sc != sc or new_ec != ec):
                            need_to_add = True
                if not used or need_to_add:
                    new_res.append((sr, sc, ec))      
            #print(new_res)
            findMaxRec(row + 1, new_res, matrix)
        findMaxRec(0, [], matrix)
        return maxRec
