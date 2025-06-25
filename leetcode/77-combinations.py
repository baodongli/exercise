class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def combinations(nums, k, prefix):
            nonlocal res
            #print(nums, k, prefix)
            if k == len(nums):
                res.append(prefix + nums)
                return
            if k == 0:
                res.append(prefix)
                return
            for i in range(0, len(nums) - k + 1):
                combinations(nums[i+1:], k-1, prefix + [nums[i]])
        combinations([i+1 for i in range(n)], k, [])
        return res
