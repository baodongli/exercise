class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n, result):
            if n in result:
                return result[n]
            if n == 0:
                result[0] = 1.0
                return 1.0
            if n == 1:
                result[1] = x
                return x
            if n < 0:
                return 1 / pow(x, -n, result)
            v = pow(x, n >> 1, result)
            result[n >> 1] = v
            if n % 2 == 0:
                result[n] = v * v
            else:
                result[n] = v * v * x
            return result[n]

        return pow(x, n, {})
