class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result_len = 0
        start1 = 0
        len1 = len(nums1)
        start2 = 0
        len2 = len(nums2)

        mpos = (len1 + len2) // 2
        odd = (len1 + len2) % 2
        self.left_val = 0
        self.left_set = False
        self.right_val = 0
        self.median = 0

        def checkMedian(result_len, prev_len, start, nums):
            if odd:
                if result_len >= mpos + 1:
                    median_pos = start + mpos - prev_len
                    self.median = (nums[median_pos])
                    return True
            else:
                if not self.left_set and result_len >= mpos:
                    self.left_val = nums[start + mpos -1 - prev_len]
                    self.left_set = True

                if result_len >= mpos + 1:
                    self.right_val = nums[start + mpos - prev_len]
                    self.median = (self.left_val + self.right_val) / 2
                    return True

            return False

        while start1 < len1 and start2 < len2:
            if nums1[start1] > nums2[start2]:
                pos = start2 + bisect_right(nums2[start2:], nums1[start1])
                prev = result_len
                result_len += pos - start2
                if checkMedian(result_len, prev, start2, nums2):
                    return self.median
                start2 = pos
            else:
                pos = start1 + bisect_right(nums1[start1:], nums2[start2])
                prev = result_len
                result_len += pos - start1
                if checkMedian(result_len, prev, start1, nums1):
                    return self.median
                start1 = pos

        # if we are here, one of the arrays is finished
        if start1 < len1:
            checkMedian(len1+len2, result_len, start1, nums1)
            return self.median

        if start2 < len2:
            checkMedian(len1+len2, result_len, start2, nums2)
            return self.median

s = Solution()
print(s.findMedianSortedArrays([1,3], [2,7]))
#print(s.findMedianSortedArrays([1,2], [3,4]))
