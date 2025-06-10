class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j = 0
        first = 0
        p = 0

        u = 1
        for n in range(1, len(needle)):
            if needle[n] == needle[0]:
                break
            u += 1

        while first <= len(haystack) - len(needle):
            if haystack[p] == needle[j]:
                j += 1
                p += 1
                if j == len(needle):
                    return first
            else:
                if j > 0: 
                    first += min(u, j)
                else:
                    first += 1
                j = 0
                p = first
        return -1
