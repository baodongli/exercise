class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def findPath(nr, nc, row, col, og, pathAt):
            if (row, col) in pathAt:
                return pathAt[(row, col)]
            if og[row][col] == 1:
                pathAt[(row, col)] = 0
                return 0
            if row == nr and col == nc:
                return 1
            
            downs = 0
            if row < nr:
                downs = findPath(nr, nc, row + 1, col, og, pathAt)
            rights = 0
            if col < nc:
                rights = findPath(nr, nc, row, col+1, og, pathAt)
            pathAt[(row, col)] = downs + rights
            return pathAt[(row, col)]
        return findPath(len(obstacleGrid)-1, len(obstacleGrid[0])-1, 0, 0, obstacleGrid, {})
