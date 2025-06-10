class Solution:
    def isValid(self, s: str) -> bool:
        pstack = []
        for c in s:
            if not pstack:
                pstack.append(c)
            else:
                if c == ')':
                    if pstack[-1] != '(':
                        return False
                    pstack.pop()
                elif c == ']':
                    if pstack[-1] != '[':
                        return False
                    pstack.pop()
                elif c == '}':
                    if pstack[-1] != '{':
                        return False
                    pstack.pop()
                else:
                    pstack.append(c)
        return True if not pstack else False
