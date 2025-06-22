class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        found = False
        for row in range(m):
            if target >= matrix[row][0] and target <= matrix[row][n-1]:
                found = True
                break
        if found:
            r = matrix[row]
            start = 0
            end = n - 1
            while start <= end:
                mid = (start + end) // 2
                #print(start, end, mid)
                if target > r[mid]:
                    start += 1
                elif target < r[mid]:
                    end -= 1
                else:
                    return True
            return False
        return False
