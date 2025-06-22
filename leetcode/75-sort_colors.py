class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1

        p0 = 0
        p2 = len(nums) - 1
        while i < j:
            # print(p0, p2, i, j, nums)
            while i <= j and (nums[i] == 0 or nums[i] == 1):
                if nums[i] == 0:
                    nums[i], nums[p0] = nums[p0], nums[i]
                    p0 += 1
                i += 1
            while i <= j and (nums[j] == 2 or nums[j] == 1):
                if nums[j] == 2:
                    nums[j], nums[p2] = nums[p2], nums[j]
                    p2 -= 1
                j -= 1
            # print(p0, p2, i, j, nums)
            # when it comes to here, num[i] = 2 and num[j] = 0
            if i < j:
                if i == p0 and j == p2:
                    nums[p2], nums[p0] = nums[p0], nums[p2]
                else:
                    # the order of the two swaps is significant
                    # if i == p0 or j == p2
                    if i == p0:
                        nums[p2], nums[i] = nums[i], nums[p2]
                        nums[p0], nums[j] = nums[j], nums[p0]
                    else:
                        nums[p0], nums[j] = nums[j], nums[p0]
                        nums[p2], nums[i] = nums[i], nums[p2]

                    if i != p0:
                        p0 += 1
                    if j != p2:
                        p2 -= 1
