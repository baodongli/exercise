class Solution:
    def myAtoi(self, s: str) -> int:
        ds = s.strip()
        if len(ds) == 0:
            return 0
        negative = False
        idx = 0
        if ds[0] == '-':
            idx = 1
            negative = True
        elif ds[0] == '+':
            idx = 1

        result = 0
        min_neg = -2 ** 31
        max_val = 2 ** 31 - 1
        while idx < len(ds) and ds[idx] >= '0' and ds[idx] <= '9':
            result = result * 10 + (ord(ds[idx]) - ord('0'))
            if negative:
                if -result <  min_neg:
                    return min_neg
            elif result > max_val:
                return max_val
            idx += 1
        return -result if negative else result
