class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        start = 0
        for i in range(1, len(s)):
            odd_cur_len = 1
            odd_cur_start = i - 1
            even_cur_len = 0
            even_cur_start = i - 1
            odd_done = False
            even_done = False

            for j in range(i - 1, -1, -1):
                right_i = 2 * i - j
                if not odd_done and right_i < len(s) and s[j] == s[right_i]:
                    odd_cur_len += 2
                    odd_cur_start = j
                else:
                    odd_done = True

                right_i = 2 * i - j - 1
                if not even_done and right_i < len(s) and s[j] == s[right_i]:
                    even_cur_len += 2
                    even_cur_start = j
                else:
                    even_done = True
                if odd_done and even_done:
                    break

            if odd_cur_len >= even_cur_len:
                if odd_cur_len > max_len:
                    start = odd_cur_start
                    max_len = odd_cur_len
            else:
                if even_cur_len > max_len:
                    start = even_cur_start
                    max_len = even_cur_len

        return s[start:max_len + start]

s = Solution()
print(s.longestPalindrome('tfekavrnnptlawqponffseumswvdtjhrndkkjppgiajjhklqpskuubeyofqwubiiduoylurzlorvnfcibxcjjzvlzfvsvwknjkzwthxxrowidmyudbtquktmyunoltklkdvzplxnpkoiikfijgulbxfxhaxnldvwmzpgaiumnvpdirlrutsqenwtihptnhghobrmmzcsrhqgdgzrvvitzgsolsxjxfeencvpnltxeetmtzlwnhlvgtbhkicivylfjhhfqteyxewmnewhmsnfdyneqoywgsgptwdlzbraksgajciebdchindegdfmayvfkwwkkfyxqjcv'))
