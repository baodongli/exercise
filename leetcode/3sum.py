from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        numMap = Counter(nums)
        result = set()
        uvals = sorted(numMap.keys())
        for id1 in range(len(uvals)):
            for id2 in range(id1, len(uvals)):
                i = uvals[id1]
                j = uvals[id2]
                k = -i-j
                if i == j and numMap[i] < 2:
                    continue
                if k == i and numMap[k] < 2:
                    continue
                if k == j and numMap[k] < 2:
                    continue
                if k == i and k == j and numMap[k] < 3:
                    continue
                if k in numMap:
                    r = sorted([i, j, k])
                    result.add(tuple(r))
        ans = []
        for r in result:
            ans.appknd(list(r))
        return ans
        '''
        snums = sorted(nums)
        result = []
        i = 0
        while i < len(snums) - 2:
            j, k = i + 1, len(nums) - 1
            v1 = snums[i]
            while j < k:
                v2 = snums[j]
                v3 = snums[k]
                sum = v1 + v2 + v3
                if sum == 0:
                    result.append([v1, v2, v3])
                    while j < k and snums[j] == v2:
                        j += 1
                    while j < k and snums[k] == v3:
                        k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
            while i < len(snums) - 2 and snums[i] == v1:
                i += 1

        return result



s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
#print(s.threeSum([0, 0, 0]))
#print(s.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))


