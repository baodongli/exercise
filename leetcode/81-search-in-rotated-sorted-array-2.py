class Solution:
    def find(self, nums, start, end, target):
        if start > end:
            return False
        m = (start + end) // 2
        if nums[m] == target:
            return True
        if nums[m] > target:
            left = m - 1
            while left >= start and nums[left] == nums[m]:
                left -= 1
            found = self.find(nums, start, left, target)
            if not found:
                right = m + 1
                while right <= end and nums[right] == nums[m]:
                    right += 1
                found = self.find(nums, right, end, target)
            return found
        else:
            right = m + 1
            while right <= end and nums[right] == nums[m]:
                right += 1
            found = self.find(nums, right, end, target)
            if not found:
                left = m - 1
                while left >= start and nums[left] == nums[m]:
                    left -= 1
                found = self.find(nums, start, left, target)
            return found

    def search(self, nums: List[int], target: int) -> int:
        return self.find(nums, 0, len(nums) - 1, target)
