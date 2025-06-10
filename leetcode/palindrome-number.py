class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ds = str(x)

        for i in range(0, len(ds) // 2):
            if ds[i] != ds[len(ds) - i - 1]:
                return False
        return True
