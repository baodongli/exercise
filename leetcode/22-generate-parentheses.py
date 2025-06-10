class Solution:
    def _generate(self, pstr, left_rem, right_rem, result):
        if left_rem == 0 and right_rem == 0:
            result.append(pstr)
            return
        if right_rem > left_rem:
            self._generate(pstr + ')', left_rem, right_rem - 1, result)
        if left_rem > 0:
            self._generate(pstr + '(', left_rem - 1, right_rem, result)

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self._generate('(', n - 1, n, result)
        return result
