class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        max_amount = 0
        '''
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                amount = min(height[i], height[j]) * (j - i)
                max_amount = max(max_amount, amount)
        return max_amount
        '''
        left = 0
        right = len(height) - 1
        while left != right:
            amount = min(height[left], height[right]) * (right - left)
            max_amount = max(amount, max_amount)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_amount
