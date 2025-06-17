class Solution:
    '''
    def getPermutation(self, n: int, k: int) -> str:
        count = 0
        base_seq = [i for i in range(1, n+1)]
        def kthPerm(seq, k, prefix):
            nonlocal count
            if not seq:
                count += 1
                if count == k:
                    return prefix
                return []
            for i in range(len(seq)):
                new_seq = kthPerm(seq[:i] + seq[i+1:], k, prefix + [seq[i]])
                if new_seq:
                    return new_seq
        return ''.join(map(str, kthPerm(base_seq, k, [])))
    '''
    '''
    def getPermutation(self, n: int, k: int) -> str:
        def getStartNum(n, k):
            factorials = 1
            for i in range(1, n):
                factorials *= i
            
            start_num = 0
            while k > (start_num + 1) * factorials:
                start_num += 1
            count = start_num * factorials
            #print(n, k, start_num, count)
            return start_num, count

        def kthPerm(seq, start_num, k, prefix):
            nonlocal count
            #print(seq, start_num, k, prefix)
            if not seq:
                return prefix
            new_start_num, new_start_count = getStartNum(len(seq) - 1, k)
            return kthPerm(seq[:start_num] + seq[start_num+1:], new_start_num, k - new_start_count, prefix + [seq[start_num]])

        base_seq = [i for i in range(1, n+1)]
        start_num, count = getStartNum(n, k)
        
        return ''.join(map(str, kthPerm(base_seq, start_num, k - count, [])))
    '''
    def getPermutation(self, n: int, k: int) -> str:
        def getStartNum(n, k):
            factorials = 1
            for i in range(1, n):
                factorials *= i
            
            start_num = 0
            while k > (start_num + 1) * factorials:
                start_num += 1
            count = start_num * factorials
            return start_num, count

        seq = [i for i in range(1, n+1)]
        rem = k
        prefix = []
        while seq:
            start_num, count = getStartNum(len(seq), rem)
            prefix.append(seq[start_num])
            seq = seq[:start_num] + seq[start_num+1:]
            rem = rem - count
        return ''.join(map(str, prefix))
