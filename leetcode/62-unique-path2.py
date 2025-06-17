class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def findPath(m, n, row, col, pathAt):
            if (row, col) in pathAt:
                return pathAt[(row, col)]
            if row == m and col == n:
                return 1
            downs = rights = 0
            if row < m:
                downs = findPath(m, n, row+1, col, pathAt)
            if col < n:
                rights = findPath(m, n, row, col+1, pathAt)
            pathAt[(row, col)] = downs + rights
            return downs + rights
        return findPath(m, n, 1, 1, {})
