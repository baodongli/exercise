class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        for r in range(9):
            row = board[r]
            # r = ['.' for _ in range(9)]
            bitmap = 0
            for v in row:
                if v != '.':
                    index = int(v) - 1
                    bit = 0x1 << index
                    if bitmap & bit:
                        return False
                    bitmap |= bit
                    #if  r[index] != '.':
                    #    return False
                    #r[index] = v
        for col in range(9):
            bitmap = 0
            for r in board:
                if r[col] != '.':
                    index = int(r[col]) - 1
                    bit = 0x1 << index
                    if bitmap & bit:
                        return False
                    bitmap |= bit
        for gr in range(0, 9, 3):
            for gc in range(0, 9, 3):
                bitmap = 0
                for r in range(3):
                    for c in range(3):
                        row = gr + r
                        col = gc + c
                        if board[row][col] != '.':
                            index = int(board[row][col]) - 1
                            bit = 0x1 << index
                            if bitmap & bit:
                                return False
                            bitmap |= bit
        return True
        '''
        rbitmap = [0 for _ in range(9)]
        cbitmap = [0 for _ in range(9)]
        gbitmap = [0 for _ in range(9)]

        for row in range(9):
            for col in range(9):
                rb = rbitmap[row]
                cb = cbitmap[col]
                gi = (row // 3) * 3 + col // 3
                if board[row][col] != '.':
                    index = int(board[row][col]) - 1
                    bit = 0x1 << index
                    if rbitmap[row] & bit:
                        return False
                    rbitmap[row] |= bit
    
                    if cbitmap[col] & bit:
                        return False
                    cbitmap[col] |= bit
    
                    if gbitmap[gi] & bit:
                        return False
                    gbitmap[gi] |= bit
        return True
