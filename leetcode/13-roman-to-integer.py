class Solution:
    def romanToInt(self, s: str) -> int:
        pos = 0
        val = 0
        while pos < len(s):
            if s[pos] == 'M':
                n = 0
                while pos < len(s) and s[pos]  == 'M':
                    n += 1
                    pos += 1
                val = 1000 * n
            elif s[pos] == 'C':
                pos += 1
                if pos < len(s):
                    if s[pos] == 'M':
                        val += 900
                        pos += 1
                    elif s[pos] == 'D':
                        val += 400
                        pos += 1
                    else:
                        n = 1
                        while pos < len(s) and s[pos] == 'C':
                            n += 1
                            pos += 1
                        val += 100 * n
                else:
                    val += 100
            elif s[pos] == 'D':
                val += 500
                pos += 1
            elif s[pos] == 'L':
                val += 50
                pos += 1
            elif s[pos] == 'V':
                val += 5
                pos += 1
            elif s[pos] == 'X':
                pos += 1
                if pos < len(s):
                    if s[pos] == 'L':
                        pos += 1
                        val += 40
                    elif s[pos] == 'C':
                        pos += 1
                        val += 90
                    else:
                        n = 1
                        while pos < len(s) and s[pos] == 'C':
                            n += 1
                            pos += 1
                        val += 10 * n
                else:
                    val += 10
            elif s[pos] == 'I':
                pos += 1
                if pos < len(s):
                    if s[pos] == 'V':
                        val += 4
                        pos += 1
                    elif s[pos] == 'X':
                        val += 9
                        pos += 1
                    else:
                        n = 1
                        while pos < len(s) and s[pos] == 'I':
                            n += 1
                            pos += 1
                        val += n
                else:
                    val += 1

        return val
