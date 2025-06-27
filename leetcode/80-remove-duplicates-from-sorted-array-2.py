class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 0
        prev = nums[0] - 1
        dups = 0
        for i, v in enumerate(nums):
            if v != prev:
                nums[pos] = v
                pos += 1
                prev = v
                dups = 1
            elif dups < 2:
                nums[pos] = v
                pos += 1
                dups += 1
        return pos
