class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0
        
        subs = p.split("*")
        first = subs[0]
        if first != '':
            i = 0
            j = 0
            while i < len(first) and j < len(s) and (first[i] == s[j] or first[i] == '?'):
                i += 1
                j += 1
            if i < len(first):
                return False
            subs = subs[1:]

        if len(subs) == 0:
            return len(s) - len(first) == 0

        s = s[len(first):]
        # The last part is not a *
        # match from the end
        last = subs[-1]
        if last != '':
            i = len(last) - 1
            j = len(s) - 1
            while i >= 0 and j >= 0 and (last[i] == '?' or last[i] == s[j]):
                i -= 1
                j -= 1
            if i >= 0:
                return False
            subs.pop()

        # There are two substrings in total
        # anything will be matched by the '*' in between
        if len(subs) == 0:
            return True
        
        s = s[:len(s) - len(last)]
        si = 0
        # For each substring, find the first occurrence
        # The rest can be matched by '*'
        for ps in subs:
            if ps == '':
                continue
            psi = 0
            prev_si = si
            while si < len(s) and psi < len(ps):
                if (ps[psi] == s[si] or ps[psi] == '?'):
                    psi += 1
                    si += 1
                else:
                    psi = 0
                    prev_si += 1
                    si = prev_si
            if psi == len(ps):
                continue
            return False
        return True
