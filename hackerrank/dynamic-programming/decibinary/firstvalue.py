import sys
class db:
    @staticmethod
    def CalcFirstDecival(value):
        if value <= 9:
            return value
        stack = []
        val = value
        if value % 2:
            stack = [(0, 9)]
            val = value - 9
        else:
            stack = [(0, 8)]
            val = value - 8

        shift = 1
        #import pdb; pdb.set_trace()
        while val > 0:
            div = val // (2 ** shift) 
            rem = val % (2 ** shift)
            coefficient = div
            if coefficient >= 9 and rem == 0:
                coefficient = 9
                stack.append([shift, coefficient])
                val -= coefficient * (2 ** shift)
            elif rem > 0:
                shift, digit = stack.pop()
                stack.append([shift, digit - 1])
                val += 2 ** shift
            else:
                stack.append([shift, coefficient])
                val -= coefficient * (2 ** shift)
            shift += 1
        val = 0
        while stack:
            shift, digit = stack.pop()
            val += digit * (10 ** shift)
        return val

if __name__ == '__main__':
    print(db.CalcFirstDecival(int(sys.argv[1])))
