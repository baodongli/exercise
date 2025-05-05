import sys

class DeciBinarySystem:
    def __init__(self, maxValue, num_of_digits):
        self.dbValues = []
        self.maxDecival = maxValue
        self.total = 0
        #self.Populate()
        self.num_of_digits = num_of_digits
        self.dbCountTbl = [[0 for _ in range(num_of_digits + 1)] for _ in range(self.maxDecival + 1)]
        self.countBefore = [0 for _ in range(self.maxDecival + 2)]
        self.GenerateDBCountTable()
        self.decibinaries = dict()

    def GenerateRow(self, dv):
        counts = self.dbCountTbl[dv]
        counts[0] = 0
        if dv < 10:
            counts[1] = 1
        else:
            counts[1] = 0
            
        for digit in range(2, self.num_of_digits + 1):
            counts[digit] = counts[digit-1]
            count_back_dv = 2 ** (digit - 1)
            for back_digit in range(1, 10):
                back_dv = dv - back_digit * count_back_dv
                if back_dv >= 0:
                    counts[digit] += self.dbCountTbl[back_dv][digit-1]
                else:
                    break

    def GenerateDBCountTable(self):
        self.dbCountTbl[0] = [1 for _ in range(self.num_of_digits + 1)]
        self.dbCountTbl[1] = [1 for _ in range(self.num_of_digits + 1)]
        self.dbCountTbl[1][0] = 0
        for dv in range(2, self.maxDecival + 1):
            self.GenerateRow(dv)
        for dv in range(1, self.maxDecival + 2):
            self.countBefore[dv] = self.countBefore[dv - 1] + self.dbCountTbl[dv - 1][-1]
    
    def FindDecibinary(self, index):
        start = 0
        end = self.maxDecival + 1
        dv = 0

        while index > self.countBefore[end]:
            self.maxDecival += 1
            dv = self.maxDecival
            self.dbCountTbl.append([0 for _ in range(self.num_of_digits + 1)])
            self.GenerateRow(dv)
            self.countBefore.append(0)
            self.countBefore[dv] = self.countBefore[dv - 1] + self.dbCountTbl[dv - 1][-1]
            end = self.maxDecival + 1
            self.countBefore[end] = self.countBefore[end - 1] + self.dbCountTbl[end - 1][-1]
        
        for k, v in enumerate(self.dbCountTbl):
            print(k, v)
        print(self.countBefore)

        #import pdb; pdb.set_trace()
        while True:
            dv = (start + end) // 2
            if dv == start:
                break
            if index > self.countBefore[dv]:
                start = dv
            elif index <= self.countBefore[dv]:
                end = dv

        # dv is the corresponding decimal value
        dv_index = index - self.countBefore[dv]
        return self.GetDecibinaryValue(dv, dv_index)

    def GetDecibinaryValue(self, dv, dv_index):
        #import pdb; pdb.set_trace()
        if dv == 0:
            return 0

        if (dv, dv_index) in self.decibinaries:
            return self.decibinaries[(dv, dv_index)]

        dv_counts = self.dbCountTbl[dv]
        digit = 0
        '''
        start = 0
        end = self.num_of_digits
        while start != end:
            digit = (start + end) // 2
            if dv_index > dv_counts[digit]:
                start = digit + 1
            else:
                end = digit        
        '''
        while dv_counts[digit] < dv_index:
            digit += 1

        dv_count = dv_index - dv_counts[digit-1]
        count_back_dv = 2 ** (digit - 1)
        cur_digit = 1
        back_dv = dv - cur_digit * count_back_dv
        while True:
            if back_dv > 0 and dv_count > self.dbCountTbl[back_dv][digit - 1]:
                dv_count -= self.dbCountTbl[back_dv][digit- 1]
                back_dv -= count_back_dv
                cur_digit += 1
            else:
                break
        
        db = (cur_digit) * (10 ** (digit-1)) + self.GetDecibinaryValue(back_dv, dv_count)
        self.decibinaries[(dv, dv_index)] = db
        return db

    def Populate(self):
        self.dbValues = [(DeciBinary(i), 0) for i in range(self.maxDecival)]
        total = 0
        for i in range(self.maxDecival):
            dbVal, _ = self.dbValues[i]
            dbVal.FindAllDecivals(self)
            print(dbVal.value, len(dbVal.GetDecivals()))
            total += len(dbVal.GetDecivals())
            self.dbValues[i] = (dbVal, total)
        self.total = total
    
    def GetDecivals(self, value):
        try:
            dbVal, _ =  self.dbValues[value]
        except:
            import pdb; pdb.set_trace()
            pass
        return dbVal.GetDecivals()
    
class DeciBinary:
    def __init__(self, value):
        self.value = value
        self.decivals = []
        self.firstDecival = DeciBinary.CalcFirstDecival(self.value)
        self.decivals.append(self.firstDecival)
        self.lastDecival = 0
        self.CalcLastDecival()
    
    def __repr__(self):
        return f"value = {self.value}, firstDecival = {self.firstDecival}, lastDecival = {self.lastDecival}, decivals = {self.decivals}\n"

    def CalcLastDecival(self):
        shift = 0
        val = self.value
        while val != 0:
            self.lastDecival += (val & 0x1) * (10 ** shift)
            val = val >> 1
            shift += 1

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

    def GetDecivals(self):
        return self.decivals

    def FindAllDecivals(self, dbSystem):
        while self.decivals[-1] != self.lastDecival:
            self.CalcNextDecival(dbSystem)

    def CalcNextDecival(self, dbSystem):
        digits = []
        prev = self.decivals[-1]
        while prev != 0:
            digits.append(prev % 10)
            prev = prev // 10

        if len(digits) == 1:
            next = 10 + digits[0] - 2
            self.decivals.append(next)
        else:
            val = digits[0]
            digits[0] = 0
            diff = 0
            didx = 1
            while didx < len(digits):
                addVal = 2 ** didx
                if val >= addVal and digits[didx] < 9:
                    digits[didx] += 1
                    diff = val - addVal
                    break
                val +=  digits[didx] * (2 ** didx)
                digits[didx] = 0
                didx += 1

            if didx == len(digits):
                addDecival = 10 ** didx
                diff = self.value - 2 ** didx
            else:
                addDecival = 0
                for i, d in enumerate(digits):
                    addDecival += d * (10 ** i)
            dvlist = dbSystem.GetDecivals(diff)
            #print(self, diff, dvlist[0])
            self.decivals.append(addDecival + dvlist[0])   

def decibinary(x):
    db = x
    div = 10

    deci_value = 0
    shift = 0
    while db:
        digit = db % div
        db = db // div

        deci_value += digit << shift
        shift += 1 

    return deci_value
        
if __name__ == '__main__':
    '''
    decimal_to_db = {}
    for i in range(int(sys.argv[1])):
        deci_value = decibinary(i)
        if deci_value in decimal_to_db:
            decimal_to_db[deci_value].append(i)
        else:
            decimal_to_db[deci_value] = [i]

#    for k, v in decimal_to_db.items():
#        print(k, v)
    
    dbSystem = DeciBinarySystem(200)
    for i in range(60):
        decivals = dbSystem.GetDecivals(i)
        if decivals != decimal_to_db[i]:
            print(i, decivals, decimal_to_db[i])
    print(dbSystem.total)
    '''
    decimal_to_db = {}
    maxval = 0
    for i in range(1200000):
        deci_value = decibinary(i)
        maxval = max(deci_value, maxval)
        if deci_value in decimal_to_db:
            decimal_to_db[deci_value].append(i)
        else:
            decimal_to_db[deci_value] = [i]

    dbSorted = []
    for dv in range(maxval+1):
        dbSorted.extend(decimal_to_db[dv])

    dbSystem = DeciBinarySystem(31, 10)
    for xth in sys.argv[1:]:
        print(dbSystem.FindDecibinary(int(xth)))
        print(dbSorted[int(xth)-1])


    
