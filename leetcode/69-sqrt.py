class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        start = 1
        end = x
        while start <= end:
            mid =  (start + end) // 2
            if mid * mid > x:
                end = mid - 1
            elif mid * mid == x:
                return mid
            else:
                start = mid + 1
        return end
