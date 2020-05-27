def count(csum, coins):
    all_sums = []
    all_sums.append(1)
    for s in range(csum):
        all_sums.append(0)
    for c in coins:
        if c > csum:
           continue
        for s in range(c, csum + 1):
            all_sums[s] = all_sums[s] + all_sums[s - c]
            print(s, s - c, all_sums)
    return all_sums[csum]


def find_next_coin(csum, value, coin, coins):
    while coin <= len(coins) - 1:
        if value + coins[coin] <= csum:
            return coin
        coin += 1
    return None

def find_min_count(csum, coins):
    count = 0
    for i, c in enumerate(coins):
        if c < csum:
            result = [i]    
            value = c
            break;
    else:
        return 0
    print(result, value)
    minc = 2 ** 32
    maxc = 0
    while result != []:
        while value + coins[result[-1]] <= csum:
            value += coins[result[-1]]
            result.append(result[-1])
        if value == csum:
            if minc > len(result):
                minc = len(result)
            if maxc < len(result):
                maxc = len(result)
            print([coins[c] for c in result])
            count += 1
            coin = result.pop()
            value -= coins[coin]
#            import pdb; pdb.set_trace()
        else:
            coin = result[-1]
        while result != [] or coin <= len(coins) - 1:
            c = find_next_coin(csum, value, coin + 1, coins)
            if c is None:
                if result == []:
                    break
                coin = result.pop()
                value -= coins[coin]
#                if result != [] and coin != result[-1]:
#                    coin = result.pop()
#                    value -= coins[coin]
            else:
                result.append(c)
                value += coins[c]
                break
    print(count)
    print(minc, maxc)

def find_min_count2(csum, coins):
    result = [0]
    max = 2 ** 32
    for i in range(csum):
        result.append(max)
    for sumk in range(1, csum + 1):
        for i, c in enumerate(coins):
            if sumk >= c:
                minc_at_k = result[sumk - c]
                if minc_at_k != max and minc_at_k + 1 < result[sumk]:
                    result[sumk] = minc_at_k + 1
    print(result[csum])

def find_max_count2(csum, coins):
    result = [0]
    for i in range(csum):
        result.append(0)
    for sumk in range(1, csum + 1):
        for i, c in enumerate(coins):
            if sumk >= c:
                maxc_at_k = result[sumk - c]
                if maxc_at_k + 1 >= result[sumk]:
                    result[sumk] = maxc_at_k + 1
    print(result[csum])
    

def find_min_count3(csum, coins):
    if csum == 0:
        return 0
    res = 2 ** 32
    for _, v in enumerate(coins):
        if csum >= v:
            min = find_min_count3(csum - v, coins)
            if min != 2 ** 32 and res > min + 1:
                res = min + 1
    return res


def makeChange(amount, denoms, index):
    denomAmount = denoms[index]
    print(amount, denomAmount, amount % denomAmount, denoms, index)
    if index >= len(denoms) - 1:
        if amount % denomAmount == 0:
            return 1
        return 0
    ways = 0
    i = 0
    while i * denomAmount <= amount: 
        amountRemaining = amount - i * denomAmount
        ways += makeChange(amountRemaining, denoms, index+1)
        i += 1
    return ways


if __name__ == '__main__':
    find_min_count(10, [3, 2, 1])        
