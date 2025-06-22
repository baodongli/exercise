class Solution:
    '''
    def climbStairs(self, n: int) -> int:
        def climb(n, steps):
            if n <= 1:
                return 1
            if steps[n] > 0:
                return steps[n]

            steps[n] = climb(n - 1, steps) + climb(n - 2, steps)
            return steps[n]
        return climb(n, [0 for _ in range(n + 1)])
    '''
    def climbStairs(self, n: int) -> int:
        steps = [0 for _ in range(n+1)]
        steps[0] = steps[1] = 1
        for i in range(2, n + 1):
            steps[i] = steps[i - 1] + steps[i - 2]
        return steps[n]
