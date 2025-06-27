class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        def checkScramble(s1, s2, res):
            #print(s1, s2)
            if (s1, s2) in res:
                return res[(s1, s2)]
            if len(s1) == 1:
                res[(s2, s1)] = res[(s1, s2)] = s1[0] == s2[0]
                return res[(s1, s2)]
            c1 = Counter(s1)
            c2 = Counter(s2)
            if c1 != c2:
                res[(s1, s2)] = res[(s2, s1)] = False
                return False
            if len(s1) == 2:
                res[(s1, s2)] = res[(s2, s1)] = True
                return True
            scrambled = False
            for i in range(1, len(s1)):
                scrambled = checkScramble(s1[:i], s2[:i], res) and \
                   checkScramble(s1[i:], s2[i:], res)
                if not scrambled:
                   scrambled = checkScramble(s1[:i], s2[-i:], res) and \
                   checkScramble(s1[i:], s2[:(len(s1)-i)], res)
                if scrambled:
                    break
            res[(s1, s2)] = res[(s2, s1)] = scrambled
            return scrambled
        return checkScramble(s1, s2, {})
