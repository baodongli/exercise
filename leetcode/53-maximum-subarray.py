class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = 0
        sum = 0
        end = 0
        max_sum = -math.inf
        cur_start = cur_end = 0
        for i, value in enumerate(nums):
            new_sum = sum + value
            if new_sum < 0:
                cur_start = cur_end = i + 1
                sum = 0
            else:
                sum = new_sum
                cur_end += 1
            if new_sum > max_sum:
                start = cur_start
                max_sum = new_sum
                end = cur_end
        
        print(start, end)
        return max_sum
