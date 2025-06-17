class Solution:
    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        def findMinSum(nr, nc, row, col, grid, minAt):
            if (row, col) in minAt:
                return minAt[(row, col)]
            if row == nr and col == nc:
                minAt[(row, col)] = grid[nr][nc]
                return grid[nr][nc]
            downMin = math.inf
            if row < nr:
                downMin = findMinSum(nr, nc, row+1, col, grid, minAt)
            rightMin = math.inf
            if col < nc:
                rightMin = findMinSum(nr, nc, row, col+1, grid, minAt)
            minAt[(row, col)] = grid[row][col] + min(downMin, rightMin)
            return minAt[(row, col)]
        return findMinSum(len(grid)-1, len(grid[0])-1, 0, 0, grid, {})
    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        minAt = [[math.inf for _ in range(nc+1)] for _ in range(nr+1)]
        for row in range(nr-1, -1, -1):
            c_start = nc - 1
            if row == nr - 1:
                minAt[row][c_start] = grid[row][c_start]
                c_start -= 1
            for col in range(c_start, -1, -1):
                downMin = minAt[row+1][col]
                rightMin = minAt[row][col+1]
                minAt[row][col] = grid[row][col] + min(downMin, rightMin)
        return minAt[0][0]
