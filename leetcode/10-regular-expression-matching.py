class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 and len(p) == 0:
            return True
        si, pi = 0, 0
        while si < len(s) and pi < len(p):
            ap = ''
            cpi = pi
            anymatch = False
            while cpi < len(p) - 1:
                if p[cpi + 1] == '*':
                    if p[cpi] == '.':
                        anymatch = True
                    ap += p[cpi]
                    cpi += 2
                else:
                    break
            if ap != '':
                must_match = ''
                if cpi < len(p):
                    must_match = p[cpi]
                    pi = cpi + 1
                else:
                    pi = cpi
                id = 0
                if must_match == '':
                    if anymatch:
                        return True
                    while si < len(s) and id < len(ap):
                        if s[si] == ap[id]:
                            si += 1
                        else:
                            id += 1
                else:
                    match = False
                    while si < len(s) and id < len(ap):
                        if (must_match == '.' or s[si] == must_match) \
                            and self.isMatch(s[si+1:], p[cpi+1:]):
                            match = True
                            break
                        if not anymatch:
                            if s[si] == ap[id]:
                                si += 1
                            elif s[si] not in ap:
                                return False
                            else:
                                id += 1
                        else:
                            si += 1
                    return match
            elif s[si] == p[pi] or p[pi] == '.':
                si += 1
                pi += 1
            else:
                break
                
        if si < len(s):
            return False
        while pi < len(p) - 1:
            if p[pi + 1] != '*':
                break
            pi += 2

        return pi == len(p)
