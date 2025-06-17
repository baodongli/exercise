class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        start = newInterval[0]
        end = newInterval[1]
        res = []
        nexti = 0
        inserted = False
        for i, v in enumerate(intervals):
            if start <= v[0]:
                res.append(newInterval)
                nexti = i
                inserted = True
                break
            
            if start <= v[1]:
                inserted = True
                res.append(v)
                if end >= v[1]:
                    v[1] = end
                nexti = i + 1
                break
            else:
                res.append(v)
        if not inserted:
            res.append(newInterval)
            return res
        for rem in range(nexti, len(intervals)):
            cur_start = res[-1][0]
            cur_end = res[-1][1]
            this_start = intervals[rem][0]
            this_end = intervals[rem][1]
            if this_start <= cur_end:
                if this_end > cur_end:
                    res[-1][1] = this_end
            else:
                res.append(intervals[rem])
        return res
