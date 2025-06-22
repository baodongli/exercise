class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for d in range(len(digits) - 1, -1, -1):
            sum = digits[d] + c
            if sum == 10:
                digits[d] = 0
                c = 1
            else:
                digits[d] = sum
                c = 0
        if c == 1:
            digits.insert(0, 1)
        return digits

