class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest_rec = 0
        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                r = stack.pop()  
                if not stack:
                    area = i * heights[r]
                else:
                    area = (i - stack[-1] - 1) * heights[r]
                largest_rec = max(largest_rec, area)
            stack.append(i)
        i = len(heights)
        while stack:
            r = stack.pop()  
            if not stack:
                area = i * heights[r]
            else:
                area = (i - stack[-1] - 1) * heights[r]
            largest_rec = max(largest_rec, area)

        return largest_rec
