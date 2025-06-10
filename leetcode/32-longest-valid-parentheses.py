class Solution:
    '''
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        sk = []
        for c in s:
            if not sk or c == '(':
                sk.append(c)
            elif c == ')':
                if sk[-1] == '(':
                    sk.pop()
                    sk.append(2)
                elif sk[-1] == ')':
                    sk.append(c)
                else:
                    sum = 0
                    while sk and isinstance(sk[-1], int):
                        v = sk.pop()
                        sum += v
                    if not sk or sk[-1] != '(':
                        sk.append(sum)
                        sk.append(c)
                    elif sk[-1] == '(':
                        sk.pop()
                        sk.append(sum+2)

        lvp = 0
        while sk:
            sum = 0
            if isinstance(sk[-1], int):
                while sk and isinstance(sk[-1], int):
                    v = sk.pop()
                    sum += v
                lvp = max(lvp, sum)
            else:
                sk.pop()
        return lvp
    '''
    '''
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        sk = []
        len_sk = [(-10, -9, 0)]
        for i, c in enumerate(s):
            if not sk or c == '(':
                sk.append((i, c))
            elif c == ')':
                pi, pc = sk[-1]
                if pc == '(':
                    sk.pop()
                    s, e, sum = len_sk[-1]
                    if pi - e == 1:
                        len_sk[-1] = s, pi+1, sum+2
                    elif s - pi == 1:
                        len_sk[-1] = pi, i, sum+2
                    else:
                        if i - pi > 1:
                            while s > pi:
                                len_sk.pop()
                                s, _, _ = len_sk[-1]
                        len_sk.append((pi, i, i - pi + 1))
                elif pc == ')':
                    sk.append((pi, pc))
        len_sk = len_sk[1:]
        if len(len_sk) == 0:
            return 0
        s, e, lvp = len_sk[0]
        if len(len_sk) <= 1:
            return lvp
        sum = lvp
        for ns, ne, l in len_sk[1:]:
            if ns - e == 1 or s - ns == 1:
                sum += l
            else:
                lvp = max(lvp, sum)
                sum = l
                s = ns
            e = ne
        lvp = max(lvp, sum)
        return lvp
    '''
    '''
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        sk = []
        cur_len = 0
        for c in s:
            if not sk or c == '(':
                if cur_len > 0:
                    sk.append(cur_len)
                    cur_len = 0
                sk.append(c)
            elif c == ')':
                if sk[-1] == '(':
                    sk.pop()
                    # sk.append(2)
                    cur_len += 2
                elif sk[-1] == ')':
                    sk.append(cur_len)
                    sk.append(c)
                    cur_len = 0
                else:
                    sum = cur_len
                    while sk and isinstance(sk[-1], int):
                        v = sk.pop()
                        sum += v
                    if not sk or sk[-1] != '(':
                        sk.append(sum)
                        sk.append(c)
                        cur_len = 0
                    elif sk[-1] == '(':
                        sk.pop()
                        cur_len = sum + 2
        sk.append(cur_len)
        lvp = 0
        while sk:
            sum = 0
            if isinstance(sk[-1], int):
                while sk and isinstance(sk[-1], int):
                    v = sk.pop()
                    sum += v
                lvp = max(lvp, sum)
            else:
                sk.pop()
        return lvp
    '''
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        leftCount = rightCount = 0
        lvp = 0
        cur_len = 0
        for i, c in enumerate(s):
            if c == '(':
                leftCount += 1
            else:
                rightCount += 1
            if rightCount > leftCount:
                leftCount = rightCount = 0
            elif rightCount == leftCount:
                cur_len = leftCount << 1
                #print("left:", cur_len, leftCount, lvp)
                lvp = max(lvp, cur_len)
            
        cur_len = 0
        leftCount = rightCount = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                rightCount += 1
            else:
                leftCount += 1
            if leftCount > rightCount:
                leftCount = rightCount = 0
            elif leftCount == rightCount:
                cur_len = rightCount << 1
                # print("right:", cur_len, rightCount, lvp)
                lvp = max(lvp, cur_len)
        return lvp
    '''
    def longestValidParentheses(self, s: str) -> int:
        # Get the length of the input string
        string_length = len(s)
        # Initialize a DP array with zeros, one extra for the base case
        dp = [0] * (string_length + 1)
    
        # Loop over the characters of string starting from index 1 for convenience
        for index, char in enumerate(s, 1):
            # We look for closing parentheses, as they mark possible ends of valid substrings
            if char == ")":
                # If the previous char is '(', it's a pair "()"
                if index > 1 and s[index - 2] == "(":
                    # Add 2 to the result two positions ago in dp array
                    dp[index] = dp[index - 2] + 2
                else:
                    # Get the index of the potential matching '('
                    match_index = index - dp[index - 1] - 1
                    # Make sure match_index is within bounds and check for '('
                    if match_index > 0 and s[match_index - 1] == "(":
                        # Add the length of the valid substring ending right before the current one,
                        # plus two for the '()' just found, plus length of valid substring before the pair
                        dp[index] = dp[index - 1] + 2 + dp[match_index - 1]
    
        # Return the maximum length of valid parentheses found
        return max(dp)
    '''
    '''
    def longestValidParentheses(self, s: str) -> int:
        stack, ans = [-1], 0
        for i in range(len(s)):
            if s[i] == '(': stack.append(i)
            elif len(stack) == 1: stack[0] = i
            else:
                stack.pop()
                ans = max(ans, i - stack[-1])
        return ans
    '''
