class Solution:
    '''
    def simplifyPath(self, path: str) -> str:
        # root
        if len(path) == 1:
            return path
        i = 1
        res = path[0]
        dirnames = []
        while i < len(path):
            if path[i] == '.':
                start = i
                while i < len(path) and path[i] == '.':
                    i += 1
                if i < len(path) and path[i] != '/':
                    while i < len(path) and path[i] != '/':
                        i += 1
                    dirnames.append(path[start:i])
                    continue

                if i - start == 1:
                    continue
                # ..
                if i - start == 2:
                    if dirnames:
                        dirnames.pop()
                else:
                    dirnames.append(path[start:i])
            elif path[i] != '/':
                start = i
                while i < len(path) and path[i] != '/':
                    i += 1
                dirnames.append(path[start:i])
            else:
                i += 1
        return '/' + '/'.join(dirnames)
    '''
    '''
    def simplifyPath(self, path: str) -> str:
        # root
        if len(path) == 1:
            return path
        i = 1
        dirnames = []
        while i < len(path):
            if path[i] != '/':
                start = i
                while i < len(path) and path[i] != '/':
                    i += 1
                dirnames.append(path[start:i])
            else:
                i += 1
        res = []
        for d in dirnames:
            if d == '.':
                continue
            if d == '..':
                if res:
                    res.pop()
                continue
            res.append(d)
        return '/' + '/'.join(res)  
    '''
    def simplifyPath(self, path: str) -> str:
        # root
        if len(path) == 1:
            return path
        dirnames = path.split('/')
        res = []
        for d in dirnames:
            if d == '.':
                continue
            if d == '..':
                if res:
                    res.pop()
                continue
            if d != '':
                res.append(d)
        return '/' + '/'.join(res)
