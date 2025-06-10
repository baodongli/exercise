class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        start = 0
        for i in range(1, len(s)):
            cur_len = 1
            cur_start = i - 1
            for j in (i - 1, -1, -1):
                right_i = 2 * i - j
                if right_i < len(s) and s[j] == s[right_i]:
                    cur_len += 2
                    cur_start = j
                else:
                    break
            if cur_len > max_len:
                start = cur_start
                max_len = cur_len
            
            cur_len = 0
            cur_start = i - 1
            for j in r(i - 1, -1, -1):
                right_i = 2 * i - j - 1
                if right_i < len(s) and s[j] == s[right_i]:
                    cur_len += 2
                    cur_start = j
                else:
                    break
            if cur_len > max_len:
                start = cur_start
                max_len = cur_len
            
        return s[start:max_len + start]
