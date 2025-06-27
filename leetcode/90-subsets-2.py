class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def getSubsetsWithDup(nums):
            if not nums:
                return [[]] 
        
            v = nums[0]
            i = 1
            while i < len(nums) and nums[i] == v:
                i += 1
            subsets = getSubsetsWithDup(nums[i:])
            new_ss = subsets.copy()
            toAdd = []
            for k in range(i):
                toAdd.append(v)
                for ss in subsets:
                    nss = ss.copy()
                    nss.extend(toAdd)
                    new_ss.append(nss)
            return new_ss
        nums.sort()
        return getSubsetsWithDup(nums)
