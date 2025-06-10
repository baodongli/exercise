class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        lcp = ''
        i = 0
        while  i < len(strs[0]):
            for s in strs[1: ]:
                if i >= len(s) or s[i] != strs[0][i]:
                    return lcp
            lcp += strs[0][i]
            i += 1
        return lcp
