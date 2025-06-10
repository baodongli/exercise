class Solution:
    def find(self, nums, start, end, target):
        if start > end:
            return -1, -1
        m = (start + end) // 2
        left = right = m 
        if target == nums[m]:
            if m - 1 >= 0 and target == nums[m - 1]:
                left, _ = self.find(nums, start, m - 1, target)
            if m + 1 < len(nums) and target == nums[m + 1]:
                _, right = self.find(nums, m + 1, end, target)
        elif target > nums[m]:
            left, right = self.find(nums, m + 1, end, target) 
        else:
            left, right = self.find(nums, start, m - 1, target) 

        return left, right

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.find(nums, 0, len(nums) - 1, target)
