class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        ss = self.subsets(nums[1:])
        new_ss = []
        #print(nums, ss)
        for s in ss:
            ns = s.copy()
            ns.append(nums[0])
            new_ss.append(ns)
        new_ss.extend(ss)
        #print(new_ss)
        return new_ss
