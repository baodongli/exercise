class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda item: item[0])
        result = [intervals[0]]
        for i in intervals[1:]:
            start = result[-1][0]
            end = result[-1][1]
            if i[0] <= end:
                if i[1] >= end:
                    result[-1] = [start, i[1]]
            else:
                result.append(i)
        return result
