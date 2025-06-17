class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        row = 0
        col = 0
        dir = 'right'
        topRowStop = 0
        bottomRowStop = n - 1
        leftColStop = 0
        rightColStop = n - 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        value = 1
        while True:
            #print(n, row, col, value)
            #print(topRowStop, bottomRowStop, leftColStop, rightColStop)
            matrix[row][col] = value
            value += 1

            if dir == 'right':
                next_col = col + 1
                if next_col > rightColStop:
                    topRowStop += 1
                    row += 1
                    if row > bottomRowStop:
                        break
                    dir = 'down'
                else:
                    col = next_col
            elif dir == 'down':
                next_row = row + 1
                if next_row > bottomRowStop:
                    rightColStop -= 1
                    col -= 1
                    if col < leftColStop:
                        break
                    dir = 'left'
                else:
                    row = next_row
            elif dir == 'left':
                next_col = col - 1
                if next_col < leftColStop:
                    bottomRowStop -= 1
                    row -= 1
                    if row < topRowStop:
                        break
                    dir = 'up'
                else:
                    col = next_col
            elif dir == 'up':
                next_row = row - 1
                if next_row < topRowStop:
                    leftColStop += 1
                    col += 1
                    if col > rightColStop:
                        break
                    dir = 'right'
                else:
                    row = next_row
        return matrix
