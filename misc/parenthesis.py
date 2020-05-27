def print_paren(l, r, pstr, index):
    print("print_paren(%s, %s, %s, %s)" % (l, r, pstr, index))
    if l < 0 or r < l:
        return
    if l == 0 and r == 0:
        print("".join(pstr))
        return
    pstr[index] = '('
    print_paren(l-1, r, pstr, index + 1)
    pstr[index] = ')'
    print_paren(l, r-1, pstr, index + 1)

def print_paren2(l, r, pstr):
    print("print_paren(%s, %s, %s)" % (l, r, pstr))
    if l < 0 or r < l:
        return
    if l == 0 and r == 0:
        print("".join(pstr))
        return
    new_pstr = copy.deepcopy(pstr)
    new_pstr.append('(')
    print_paren2(l - 1, r, new_pstr)
    new_pstr = copy.deepcopy(pstr)
    new_pstr.append(')')
    print_paren2(l, r - 1, new_pstr)

def print_paren3(l, r, pstr):
    if l < 0 or r < l:
        return
    if l == 0 and r == 0:
        print("".join(pstr))
        return
    if l != 0:
        pstr.append('(')
        print_paren3(l - 1, r, pstr)
        pstr.pop()
    if r != 0:
        pstr.append(')')
        print_paren3(l, r - 1, pstr)
        pstr.pop()


l = 3
r = 3
pstr = [' ' for _ in range(l+r)]
print_paren(3, 3, pstr, 0)
