class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
#        zig_len = 2 * numRows - 2
#        cols = ((len(s) + zig_len - 1)  // zig_len) * (numRows - 1)
#        result = [['' for _ in range(cols)] for _ in range(numRows)]
        result = ['' for _ in range(numRows)]
        row = 0
        down = True
        for c in s:
            result[row] += c
            if down:
                row = (row + 1) % numRows
                if row == 0:
                    row = numRows - 2
                    down = False
            else:
                if row == 0:
                    down = True
                    row = 1
                else:
                    row -= 1

        out = ''.join(result)
#        for r in range(numRows):
#            out += result[r]
        return out

s = Solution()
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))
