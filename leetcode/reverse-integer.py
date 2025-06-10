class Solution:
    def reverse(self, x: int) -> int:
        val = x
        result = 0
        if x < 0:
            val = -x
        while val > 0:
            result = val % 10 + result * 10
            val //= 10

        if x < 0:
            result = -result
        return result if (result <= (2 ** 31 - 1) and result >= (-2 ** 31)) else 0


s = Solution()
print(s.reverse(1534236469))
