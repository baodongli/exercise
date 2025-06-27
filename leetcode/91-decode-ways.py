kclass Solution:
    def numDecodings(self, s: str) -> int:
        def getNumDecodings(s, res):
            if s in res:
                return res[s]
            if len(s) == 0:
                return 1
            if s[0] == '0':
                return 0
            if len(s) == 1:
                res[s] = 1
                return 1
            v = int(s[:2])
            n1 = getNumDecodings(s[1:], res)
            n2 = 0
            if v <= 26:
                n2 = getNumDecodings(s[2:], res)
            res[s] = n1 + n2
            return n1 + n2 
        res = {'': 1}
        return getNumDecodings(s, res)
