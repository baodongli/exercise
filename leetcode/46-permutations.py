class Solution:
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        perms = self.permute(nums[1:])
        new_perms = []
        for p in perms:
            for i in range(len(p) + 1):
                np = p.copy()
                np.insert(i, nums[0])
                # print(np)
                new_perms.append(np)
        return new_perms
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutations(nums, prefix, result):
            if not nums:
                result.append(prefix)
                return
            for i in range(len(nums)):
                permutations(nums[:i] + nums[i+1:], prefix + [nums[i]], result)
        perms = []
        permutations(nums, [], perms)
        return perms
