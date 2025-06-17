class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        topRowStop = 0
        bottomRowStop = len(matrix) - 1
        leftColStop = 0
        rightColStop = len(matrix[0]) - 1
        res = []
        row = 0
        col = 0
        dir = 'right'
        while True:
            #print(row, col)
            #print(topRowStop, bottomRowStop, leftColStop, rightColStop)
            res.append(matrix[row][col])
            if dir == 'right':
                new_col = col + 1
                if new_col > rightColStop:
                    topRowStop += 1
                    row += 1 
                    if row > bottomRowStop:
                        break
                    dir = 'down'
                else:
                    col = new_col
            elif dir == 'down':
                new_row = row + 1
                if new_row > bottomRowStop:
                    rightColStop -= 1
                    col -= 1
                    if col < leftColStop:
                        break
                    dir = 'left'
                else:
                    row = new_row
            elif dir == 'left':
                new_col = col - 1
                if new_col < leftColStop:
                    bottomRowStop -= 1
                    row -= 1 
                    if row < topRowStop:
                        break
                    dir = 'up'
                else:
                    col = new_col
            elif dir == 'up':
                new_row = row - 1
                if new_row < topRowStop:
                    leftColStop += 1
                    col += 1
                    if col > rightColStop:
                        break
                    dir = 'right'
                else:
                    row = new_row
        return re
