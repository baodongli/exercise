class Solution:
    def find(self, nums, start, end, target):
        if start > end:
            return -1
        m = (start + end) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            i = self.find(nums, start, m - 1, target)
            if i < 0:
                return self.find(nums, m + 1, end, target)
            else:
                return i
        else:
            i = self.find(nums, m + 1, end, target)
            if i < 0:
                return self.find(nums, start, m - 1, target)
            else:
                return i


    def search(self, nums: List[int], target: int) -> int:
        return self.find(nums, 0, len(nums) - 1, target)
