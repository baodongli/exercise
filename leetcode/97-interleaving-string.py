class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            return False
        c1 = Counter(s1)
        c1.update(s2)
        c3 = Counter(s3)
        if c1 != c3:
            return False

        def checkInterleave(s1, s2, s3, p1, p2, p3, which, res):
            hstr = which + str(p1) + str(p2) + str(p3)
            if hstr in res:
                return res[hstr]
            if p1 == len(s1) and p2 == len(s2) and p3 == len(s3):
                return True
            isInterleaved = False
            if which == "s1" or not which:
                l = 0
                while l + p1 < len(s1) and l + p3 < len(s3) and s1[p1+l] == s3[p3+l]:
                    isInterleaved = checkInterleave(s1, s2, s3, p1+l+1, p2, p3+l+1, 's2', res)
                    if isInterleaved:
                        break
                    l += 1
            if not isInterleaved and (which == "s2" or not which):
                l = 0
                while l + p2 < len(s2) and l + p3 < len(s3) and s2[p2+l] == s3[p3+l]:
                    isInterleaved = checkInterleave(s1, s2, s3, p1, p2+l+1, p3+l+1, 's1', res)
                    if isInterleaved:
                        break
                    l += 1
            res[hstr] = isInterleaved
            return isInterleaved
        return checkInterleave(s1, s2, s3, 0, 0, 0, "", {})
