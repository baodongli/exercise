class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chCount = Counter(t)
        chUsed = deque()
        chUsedCount = Counter("")
        chCurCount = 0

        i = 0
        start = 0
        end = len(s) + 1
        while i < len(s) or chUsed:
            if chCurCount >= len(t):
                sp = chUsed.popleft()
                sc = s[sp]
                if chUsed:
                    ep = chUsed[-1]
                else:
                    ep = sp
                if ep - sp < end - start:
                    start = sp
                    end = ep
                chUsedCount[sc] -= 1
                if chUsedCount[sc] < chCount[sc]:
                    chCurCount -= 1
            elif i < len(s):
                c = s[i]
                if c in chCount:
                    chUsedCount[c] += 1
                    if chUsedCount[c] <= chCount[c]:
                        chCurCount += 1
                    chUsed.append(i)
                i += 1
            else:
                break
        return s[start:end+1] if end < len(s) else ''
