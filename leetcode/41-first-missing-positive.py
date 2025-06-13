class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pos = 0
        while pos < len(nums):
            value = nums[pos]
            while 0 < value <= len(nums) and value != nums[value - 1]:
                nums[pos], nums[value - 1] = nums[value - 1], nums[pos]
                value = nums[pos]
            pos += 1

        # print(nums)
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        return len(nums) + 1
    '''
    use more space
    def firstMissingPositive(self, nums: List[int]) -> int:
        occured = {}
        for n in nums:
            if n > 0:
                occured[n] = True
        for i in range(1, len(nums) + 1):
            if i not in occured:
                return i
        return len(nums) + 1
    '''
