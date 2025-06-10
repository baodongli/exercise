class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        snums = sorted(nums)
        closest = math.inf
        for i in range(len(snums) - 2):
            j, k = i + 1, len(nums) - 1
            v1 = snums[i]
            while j < k:
                v2 = snums[j]
                v3 = snums[k]
                sum = v1 + v2 + v3
                diff = sum - target
                if diff == 0:
                    return target
                elif diff < 0:
                    j += 1
                    if abs(diff) < abs(closest - target):
                        closest = sum
                else:
                    k -= 1
                    if abs(diff) < abs(closest - target):
                        closest = sum
        return closest
