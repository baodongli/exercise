class Solution:
    def getQuotient(self, dividend, divisor, result):
        if dividend in result:
            return result[dividend]
        if dividend < divisor:
            result[dividend] = (0, dividend)
            return 0, dividend
        elif dividend == divisor:
            result[dividend] = (1, 0)
            return 1, 0
        halfLeft = dividend >> 1
        halfRight = dividend - halfLeft
        qL, rL = self.getQuotient(halfLeft, divisor, result)
        if halfRight == halfLeft:
            qR, rR = qL, rL
        else:
            qR, rR  = self.getQuotient(halfRight, divisor, result)

        if rL + rR >= divisor:
            q, r =  qL + qR + 1, rL + rR - divisor
        else:
            q, r = qL + qR, rL + rR
        result[dividend] = (q, r)
        return q, r

    def divide(self, dividend: int, divisor: int) -> int:
        negative = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            negative = True
        
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor

        quotient = 1
        if divisor == 1:
            quotient = dividend
        elif dividend < divisor:
            quotient = 0
        else:
            '''
            sum = divisor
            dividend -= divisor
            ssk = []
            push = True
            r = 1
            while dividend >= divisor:
                if dividend >= sum:
                    dividend -= sum
                    quotient += r
                    if push:
                        ssk.append((sum, r))
                        sum += sum
                        r += r
                else:
                    push = False
                    while dividend < sum and len(ssk):
                        sum, r = ssk.pop()
            '''
            quotient, _ = self.getQuotient(dividend, divisor, {})

        if not negative:
            if  quotient > 2 ** 31 - 1:
                return 2 ** 31 -1
            else:
                return quotient
        else:
            if quotient > 2 ** 31:
                return -2**31
            else:
                return -quotient
