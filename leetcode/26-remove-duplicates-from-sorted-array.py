class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #if len(nums) == 0:
        #    return 0
        #last = nums[0]
        k = 0
        for item in range(1, len(nums)):
            if nums[item] != nums[k]:
                k += 1
                #if pos != item:
                nums[k] = nums[item]
                #last = nums[item]
        return k + 1
