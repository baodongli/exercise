class Solution:
    def addBinary(self, a: str, b: str) -> str:
        size = min(len(a), len(b))
        rsize = max(len(a), len(b))
        c = 0
        res = []
        dtc = ['0', '1', '0', '1']
        carry = [0, 0, 1, 1]
        ra = list(reversed(a))
        rb = list(reversed(b))
        for pos in range(size):
            sum = ord(ra[pos]) + ord(rb[pos]) - 2 * ord('0') + c
            res.append(dtc[sum])
            c = carry[sum]
        r = ra if len(a) > len(b) else rb
        if c == 1:
            for pos in range(size, rsize):
                sum = ord(r[pos]) - ord('0') + c
                res.append(dtc[sum])
                c = carry[sum]
            if c == 1:
                res.append('1')
        else:
            res.extend(r[size:])
        return ''.join(reversed(res))
