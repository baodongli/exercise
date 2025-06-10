class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zig_len = 2 * numRows - 2
        cols = ((len(s) + zig_len - 1)  // zig_len) * (numRows - 1)
        result = [['' for _ in range(cols)] for _ in range(numRows)]
        row, col = 0, 0
        down = True
        for c in s:
            result[row][col] = c
            if down:
                row = (row + 1) % numRows
                if row == 0:
                    row = numRows - 2
                    down = False
                    col += 1
            else:
                if row == 0:
                    down = True
                    row = 1
                else:
                    row -= 1
                    col += 1

        out = ''
        for r in range(numRows):
            for c in range(cols):
                if result[r][c] != '':
                    out += result[r][c]
        return out

s = Solution()
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))
