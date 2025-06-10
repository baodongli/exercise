class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = dict()
        max_substr_len = 0
        cur_start = 0
        for index, c in enumerate(s):
            if c in pos and pos[c] >= cur_start:
                max_substr_len = max(max_substr_len, index - cur_start)
                cur_start = pos[c] + 1
            pos[c] = index
        return max(max_substr_len, len(s) - cur_start)
