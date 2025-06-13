class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        def combSum(index, target, comb, result):
            if target == 0:
                result.append(comb.copy())
                return
            if index >= len(candidates) or target < 0:
                return
            combSum(index + 1, target, comb, result)
            value = candidates[index]
            comb.append(value)
            combSum(index, target - value, comb, result)
            comb.pop()
        '''
        def combSum(index, target, comb, result):
            if target == 0:
                result.append(comb.copy())
                return
            if index >= len(candidates) or target < 0:
                return
            combSum(index + 1, target, comb, result)
            value = candidates[index]
            for i in range(1, target // value + 1):
                comb.extend([value] * i)
                combSum(index + 1, target - value * i, comb, result)
                del comb[-i:]
        '''
        candidates.sort()
        def combSum(index, target, comb, result):
            if target == 0:
                result.append(comb.copy())
                return
            if index >= len(candidates):
                return
            for i in range(index, len(candidates)):
                value = candidates[i]
                for j in range(1, target // value + 1):
                    comb.extend([value] * j)
                    combSum(i + 1, target - value * j, comb, result)
                    del comb[-j:]
                    
        '''
        ans = []
        combSum(0, target, [], ans)
        return ans
