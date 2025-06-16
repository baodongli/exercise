class Solution:
    ''' Time Limit Exceeded
    def jump(self, nums: List[int]) -> int:
        minJumps = math.inf
        visited = set()
        def jumpAt(index, nums, jumps):
            nonlocal minJumps, visited
            if (index, jumps) in visited:
                return
            visited.add((index, jumps))
            if index == len(nums) - 1:
                minJumps = min(minJumps, jumps)
                return
            if jumps >= minJumps:
                return
            if index + nums[index] >= len(nums) - 1:
                minJumps = min(minJumps, jumps + 1)
                return 
            for j in range(1, nums[index] + 1):
                if index + j < len(nums):
                    jumpAt(index + j, nums, jumps+1)
                else:
                    break
        jumpAt(0, nums, 0)
        return minJumps
    '''
    '''
    def jump(self, nums: List[int]) -> int:
        maxSteps = len(nums) - 1
        minJumps = [math.inf for _ in range(len(nums))]
        minJumps[maxSteps] = 0
        i = len(nums) - 2
        while i >= 0:
            if i + nums[i] >= maxSteps:
                minJumps[i] = 1
            else:
                cur_min = math.inf
                for j in range(1, nums[i] + 1):
                    cur_min = min(minJumps[i + j] + 1, cur_min)
                    if cur_min <= 2:
                        break
                minJumps[i] = cur_min
            i -= 1
        return minJumps[0]
    '''
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        cur_reach = 0
        i = 0
        next_reach = 0
        while next_reach < len(nums) - 1:
            while i <= cur_reach:
                next_reach = max(i + nums[i], next_reach)
                i += 1
            jumps += 1
            cur_reach = next_reach
        return jumps
