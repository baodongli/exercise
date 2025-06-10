from collections import Counter
import math
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        snums = sorted(nums)
        closest = math.inf
        import pdb; pdb.set_trace()
        for i in range(len(snums) - 2):
            j, k = i + 1, len(nums) - 1
            v1 = snums[i]
            while j < k:
                v2 = snums[j]
                v3 = snums[k]
                sum = v1 + v2 + v3
                diff = v1 + v2 + v3 - target
                print(v1, v2, v3, sum, diff)
                if diff == 0:
                    return target
                elif diff < 0:
                    j += 1
                    if abs(diff) < abs(closest):
                        closest = sum
                else:
                    k -= 1
                    if abs(diff) < abs(closest):
                        closest = sum
        return closest

s = Solution()
print(s.threeSumClosest([-1,2,1,-4], 1))


