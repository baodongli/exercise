class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #nums = sorted(candidates)
        counts = Counter(candidates)
        #nums = sorted(counts.keys())
        nums = list(counts.keys())
        comb = []
        def combSum2(index, target, result):
            nonlocal comb
            if target == 0:
                result.append(comb.copy())
                return
            if index >= len(nums):
                return
            combSum2(index+1, target, result)
            value = nums[index]
            count = counts[value]
            for i in range(1, count+1):
                #newcomb = comb.copy()
                #newcomb.extend([value] * i)
                nv = target - value * i
                if nv < 0:
                    break
                comb.extend([value] * i)
                #print(comb)
                combSum2(index+1, nv, result)
                del comb[-i:]
        
        ans = []
        combSum2(0, target, ans)
        return ans
    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        candidates.sort()
    
        def findCombination(ind: int, target: int):
            if target == 0:
                ans.append(ds[:])
                return
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                ds.append(candidates[i])
                findCombination(i + 1, target - candidates[i])
                ds.pop()

        findCombination(0, target)
        return ans
    '''
