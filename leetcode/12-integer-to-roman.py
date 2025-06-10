class Solution:
    def intToRoman(self, num: int) -> str:
        r, fd = divmod(num, 10)

        roman = ''
        if fd >= 1 and fd <= 3:
            roman = 'I' * fd
        elif fd == 4:
            roman = 'IV'
        elif fd == 5:
            roman = 'V'
        elif fd >= 6 and fd <= 8:
            roman = 'V' + 'I'*(fd - 5)
        elif fd == 9:
            roman = 'IX'
        
        if r == 0:
            return roman
        
        r, fd = divmod(r, 10)
        if fd >= 1 and fd <= 3:
            roman = 'X' * fd + roman
        elif fd == 4:
            roman = 'XL' + roman
        elif fd == 5:
            roman = 'L' + roman
        elif fd >= 6 and fd <= 8:
            roman = 'L' + 'X'*(fd - 5) + roman
        elif fd == 9:
            roman = 'XC' + roman

        if r == 0:
            return roman
        
        r, fd = divmod(r, 10)
        if fd >= 1 and fd <= 3:
            roman = 'C' * fd + roman
        elif fd == 4:
            roman = 'CD' + roman
        elif fd == 5:
            roman = 'D' + roman
        elif fd >= 6 and fd <= 8:
            roman = 'D' + 'C'*(fd - 5) + roman
        elif fd == 9:
            roman = 'CM' + roman

        if r == 0:
            return roman
        
        r, fd = divmod(r, 10)
        if fd >= 1 and fd <= 3:
            roman = 'M' * fd + roman

        return roman
