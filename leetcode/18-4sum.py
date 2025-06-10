class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        snums = sorted(nums)
        result = []
        a = 0
        while a < len(snums) - 3:
            b = a + 1
            while b < len(snums) - 2:
                c, d = b + 1, len(nums) - 1
                v1 = snums[a]
                v2 = snums[b]
                while c < d:
                    v3 = snums[c]
                    v4 = snums[d]
                    sum = v1 + v2 + v3 + v4
                    if sum == target:
                        result.append([v1, v2, v3, v4])
                        while c < d and snums[c] == v3:
                            c += 1
                        while c < d and snums[d] == v4:
                            d -= 1
                    elif sum < target:
                        c += 1
                    else:
                        d -= 1
                while b < len(snums) - 2 and snums[b] == v2:
                    b += 1
            while a < len(snums) - 3 and snums[a] == v1:
                a += 1

        return result
