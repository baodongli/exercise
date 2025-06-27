class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        res = []
        gcode = self.grayCode(n-1)
        addZeroFirst = True
        for gc in gcode:
            if addZeroFirst:
                res.append(gc * 2)
                res.append(gc * 2+1)
                addZeroFirst = False
            else:
                res.append(gc*2+1)
                res.append(gc*2)
                addZeroFirst = True
        return res
