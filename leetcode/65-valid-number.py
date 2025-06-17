class Solution:
    '''
    def isNumber(self, s: str) -> bool:
        pattern = re.compile(r"""
            ^[+-]?                    # optional sign
            (                        # start number group
                ( \d+ (\.\d*)? )     # digits + optional .digits
              | ( \.\d+ )            # or just .digits
            )
            ([eE][+-]?\d+)?          # optional exponent part
            $""", re.VERBOSE)
        
        return bool(pattern.match(s.strip()))
    '''
    def isNumber(self, s: str) -> bool:
        def getDigits(start, s):
            if start >= len(s):
                return -1
            while start < len(s) and ord(s[start]) >= ord('0') and ord(s[start]) <= ord('9'):
                start += 1
            return start
    
        if len(s) == 0:
            return False
        i = 0
        if s[0] == '-' or s[0] == '+':
            i += 1
            if i == len(s):
                return False
        ds = i
        decimal = False
        if s[i] == '.':
            decimal = True
            ds = i + 1
        ni = getDigits(ds, s)

        if ni < 0 or ni == ds:
            return False
        if ni == len(s):
            return True
        
        i = ni
        # too many .
        if decimal and s[i] == '.':
            return False
        
        # decimal right part
        if s[i] == '.':
            ds = i + 1
            i = getDigits(ds, s)
            if i < 0:
                return True
            if i == len(s):
                return True

        # exponent part
        if s[i] == 'e' or s[i] == 'E':
            ds = i + 1
            if ds == len(s):
                return False
            if s[ds] == '-' or s[ds] == '+':
                ds += 1

            i = getDigits(ds, s)
            if i < 0 or i == ds:
                return False
            if i == len(s):
                return True
        return False
