class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_reach = 0
        i = 0
        next_reach = 0
        while next_reach < len(nums) - 1:
            while i <= cur_reach:
                next_reach = max(i + nums[i], next_reach)
                i += 1
            if next_reach <= cur_reach and next_reach < len(nums) - 1:
                return False
            cur_reach = next_reach
        return True
