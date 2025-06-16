class Solution:
    '''
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permutations(nums, permsExisted):
            if len(nums) == 1:
                return [nums]
            perms = permutations(nums[1:], permsExisted)
            new_perms = []
            for p in perms:
                for i in range(len(p)+1):
                    np = p.copy()
                    np.insert(i, nums[0])
                    if tuple(np) not in permsExisted:
                        new_perms.append(np)
                    permsExisted[tuple(np)] = True
            return new_perms
        return permutations(nums, {})
    '''
    '''
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = []
        def permutations(nums, prefix):
            if not nums:
                perms.append(prefix)
                return
            cv = nums[0]
            permutations(nums[1:], prefix + [cv])
            for i in range(1, len(nums)):
                if nums[i] == cv:
                    continue
                permutations(nums[:i] + nums[i+1:], prefix + [nums[i]])
                cv = nums[i]
        nums.sort()
        permutations(nums, [])
        return perms
    '''
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        perms = []
        def permutations(prefix):
            if len(prefix) == len(nums):
                perms.append(prefix)
                return
            for n in counts:
                if counts[n] == 0:
                    continue
                counts[n] = counts[n] - 1
                permutations(prefix + [n])
                counts[n] = counts[n] + 1
        permutations([])
        return perms
