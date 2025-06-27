class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos = m + n - 1
        pm = m - 1
        pn = n - 1
        while pm >= 0 and pn >= 0:
            if nums1[pm] >= nums2[pn]:
                nums1[pos] = nums1[pm]
                pm -= 1
            else:
                nums1[pos] = nums2[pn]
                pn -= 1
            pos -= 1
        while pm >= 0:
            nums1[pos] = nums1[pm]
            pm -= 1
            pos -= 1
        while pn >= 0:
            nums1[pos] = nums2[pn]
            pn -= 1
            pos -= 1

