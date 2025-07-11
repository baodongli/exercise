class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dlmap = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        if len(digits) == 0:
            return []
        letcomb = dlmap[digits[0]]
        for d in digits[1:]:
            letters = dlmap[d]
            newcomb = []
            for c1 in letcomb:
                for c2 in letters:
                    newcomb.append(c1 + c2)
            letcomb = newcomb
        return letcomb
