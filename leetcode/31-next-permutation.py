class Solution:
    '''
    below also search from the right and found the last one that is less
    than the remaining. It's actually equivalent to find neighboring items
    with a[j] < a[j+1], but unnessarily complext
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        start = 0
        left = -1
        right = 0
        swap = False
        for i in range(len(nums)-1, 0, -1):
            found = False
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    found = True
                    break
            if found:
                swap = True
                if j > left:
                    left = j
                    right = i
                    start = left + 1

        if swap:
            nums[left], nums[right] = nums[right], nums[left]
        for k in range(start, len(nums) - 1):
            # stop at len(nums) + start - k - 1
            for g in range(start, len(nums) + start - k - 1):
                if nums[g] > nums[g + 1]:
                    nums[g], nums[g+1] = nums[g+1], nums[g]
        
        return nums
    '''
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        found = False
        start = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                found = True
                start = i + 1
                break
        if found:
            # swap the smallest one that is larger than nums[i]
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                    break
        # Reverse from start to end
        end = (start + len(nums)) // 2
        for left in range(start, end):
            right = start + len(nums) - left -1 
            nums[left], nums[right] = nums[right], nums[left]
        return nums
