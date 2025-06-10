class Solution:
    def find(self, nums, start, end, target):
        if start > end:
            return start
        m = (start + end) // 2
        if target == nums[m]:
            return m
        elif target > nums[m]:
            return self.find(nums, m+1, end, target)
        else:
            return self.find(nums, start, m-1, target)
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.find(nums, 0, len(nums) - 1, target)
