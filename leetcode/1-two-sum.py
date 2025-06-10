class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numCount = dict()
        for index, num in enumerate(nums):
            if target - num in numCount:
                return [numCount[target-num], index]
            numCount[num] = index
        return []
        

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))
