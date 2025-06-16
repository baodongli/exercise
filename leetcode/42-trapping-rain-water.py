class Solution:
    '''
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        # index, water trapped to the left
        stack = [(0, 0)]
        hi = 1
        tw = 0
        while hi < len(height):
            #print(stack)
            index, w = stack[-1]
            if height[hi] > height[index]:
                if len(stack) <= 1:
                    stack.pop()
                    stack.append((hi, w + tw))
                    tw = 0
                    hi += 1
                else:
                    stack.pop()
                    index1, w1 = stack[-1]
                    tw += (min(height[hi], height[index1]) - height[index]) * (hi - index1 - 1) + w
            elif height[hi] < height[index]:
                stack.append((hi, tw))
                tw = 0
                hi += 1
            else:
                stack.pop()
                stack.append((hi, w + tw))
                tw = 0
                hi += 1
        tw = 0
        #print(stack)
        while stack:
            _, w = stack.pop()
            tw += w
        return tw    
    '''
    '''
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        max_left = [0 for _ in range(len(height))]
        max_right = [0 for _ in range(len(height))]
        max_left[0] = height[0]
        max_right[len(height) - 1] = height[len(height) - 1]
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i])
        for i in range(len(height)-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])

        tw = 0
        for i in range(len(height)):
            tw += min(max_left[i], max_right[i]) - height[i]
        return tw
    '''
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        res = 0
        maxLeft = 0
        maxRight = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= maxLeft:
                    maxLeft = height[left]
                else:
                    res += maxLeft - height[left]
                left += 1
            else:
                if height[right] >= maxRight:
                    maxRight = height[right]
                else:
                    res += maxRight - height[right]
                right -= 1
        return res
