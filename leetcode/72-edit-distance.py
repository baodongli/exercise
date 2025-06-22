class Solution:
    '''
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return (len(word1) + len(word2))
        minOps = math.inf
        chAt = {}
        for pos, ch in enumerate(word1):
            if ch not in chAt:
                chAt[ch] = [0]
            chAt[ch].append(pos)
        #print(chAt)
        matches = [(-1, -1)]
        def findMinOps(pos, matches, ops, chAt):
            nonlocal minOps
            #print(pos, matches, ops, minOps)
            if pos == len(word2):
                lp1, lp2 = matches[-1]
                new_ops = max((len(word1)) - lp1 - 1, pos - lp2 - 1)
                minOps = min(ops + new_ops, minOps)
                return 0
            ch = word2[pos]
            if ch not in chAt:
                return findMinOps(pos+1, matches, ops, chAt)
            locs = chAt[ch]
            prev_loc = locs[0]
            cur_loc = prev_loc + 1
            lp1, lp2 = matches[-1]
            for loc in locs[prev_loc + 1:]:
                locs[0] = cur_loc
                cur_loc += 1
                if loc < lp1:
                    continue
                new_ops = ops + max(loc - lp1 - 1, pos - lp2 - 1)
                minMin = abs(len(word1) - loc - (len(word2) - pos))
                if new_ops + minMin >= minOps:
                    continue
                matches.append((loc, pos))
                findMinOps(pos+1, matches, new_ops, chAt)
                matches.pop()
            locs[0] = prev_loc
            findMinOps(pos+1, matches, ops, chAt)
        findMinOps(0, matches, 0, chAt)
        return minOps
    '''
    '''
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return (len(word1) + len(word2))
        chAt = {}
        for pos, ch in enumerate(word1):
            if ch not in chAt:
                chAt[ch] = [0]
            chAt[ch].append(pos)
        matches = [(-1, -1)]
        def findMinOps(pos, matches, chAt, minAt):
            if pos == len(word2):
                lp1, lp2 = matches[-1]
                return max((len(word1)) - lp1 - 1, pos - lp2 - 1)
            ch = word2[pos]
            if ch not in chAt:
                return findMinOps(pos+1, matches, chAt, minAt)
            locs = chAt[ch]
            prev_loc = locs[0]
            cur_loc = prev_loc + 1
            lp1, lp2 = matches[-1]
            cur_min = math.inf
            for loc in locs[prev_loc + 1:]:
                locs[0] = cur_loc
                cur_loc += 1
                if loc < lp1:
                    continue
                new_ops = max(loc - lp1 - 1, pos - lp2 - 1)
                minMin = abs(len(word1) - loc - (len(word2) - pos))
                if new_ops + minMin >= cur_min:
                    continue
                if (loc, pos) not in minAt:
                    matches.append((loc, pos))
                    minAt[(loc, pos)] = findMinOps(pos+1, matches, chAt, minAt)
                    matches.pop()
                cur_min = min(cur_min, new_ops + minAt[(loc, pos)])
            locs[0] = prev_loc
            nops = findMinOps(pos+1, matches, chAt, minAt)
            return min(cur_min, nops)
        return findMinOps(0, matches, chAt, {})
    '''
    def minDistance(self, word1: str, word2: str) -> int:
        lw1 = len(word1)
        lw2 = len(word2)
        if lw1 == 0 or lw2 == 0:
            return lw1 + lw2
        minOps = [[-1 for _ in range(lw1 + 1)] for _ in range(lw2 + 1)]
        minOps[0] = [i for i in range(lw1 + 1)]
        for i in range(lw2+1):
            minOps[i][0] = i
        ''' It turned out that for loop is much slower than recursion
            in Python as demonstrated below.
        for i in range(1, lw2+1):
            for j in range(1, lw1+1):
                if word1[j-1] == word2[i-1]:
                    minOps[i][j] = minOps[i-1][j-1]
                else:
                    minOps[i][j] = min(minOps[i-1][j],
                                       minOps[i][j-1],
                                       minOps[i-1][j-1]) + 1
        '''
        def findMinOps(i, j):
            if minOps[i][j] != -1:
                return minOps[i][j]
            if word1[j-1] == word2[i-1]:
                minOps[i][j] = findMinOps(i-1, j-1)
            else:
                minOps[i][j] = min(findMinOps(i-1, j),
                                   findMinOps(i, j-1),
                                   findMinOps(i-1, j-1)) + 1
            return minOps[i][j]
            
        #print(minOps)
        #return minOps[lw2][lw1]
        return findMinOps(lw2, lw1)
