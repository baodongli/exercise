'''
class Solution:
    def numTrees(self, n: int) -> int:
        def getNumTrees(left, right, countMap):
            if (right-left+1) in countMap:
                return countMap[right-left+1]
            if left > right:
                countMap[right-left+1] = 0
                return 0
            if left == right:
                countMap[right-left+1] = 1
                return 1
            count = 0
            for i in range(left, right+1):
                leftCount = getNumTrees(left, i-1, countMap)
                rightCount = getNumTrees(i+1, right, countMap)
                if leftCount > 0 and rightCount > 0:
                    count += leftCount * rightCount
                elif leftCount > 0:
                    count += leftCount
                else:
                    count += rightCount
            countMap[right-left+1] = count
            return count
        
        return getNumTrees(1, n, {})
'''
class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        count = 0
        for i in range(n):
            leftCount = self.numTrees(i)
            rightCount = self.numTrees(n - i - 1)
            if leftCount > 0 and rightCount > 0:
                count += leftCount * rightCount
            elif leftCount > 0:
                count += leftCount
            else:
                count += rightCount
        return count
