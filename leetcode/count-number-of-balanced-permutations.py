from functools import cache
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        numberCounts = {b10_num: 0 for b10_num in range(10)}
        sum = 0
        for ch in num:
            numberCounts[int(ch)] += 1
            sum += int(ch)
        
        if sum % 2 != 0:
            return 0
        
        half_sum = sum // 2
        odd_count = (len(num) + 1) // 2
        even_count = len(num) - odd_count
        nums = sorted(numberCounts.keys())
        available_numbers = []
        cur_sum = 0
        running_sum = dict()
        for number in nums:
            if numberCounts[number] != 0:
                available_numbers.append(number)
                cur_sum += numberCounts[number] * number
                running_sum[number] = cur_sum

        MOD = 10 ** 9 + 7


        result = []
        self.num_distinct_perms = 0
        @cache
        def getCount(total, number):
            count = 1
            for c in range(total, total - number, -1):
                count *= c
            div = 1
            for n in range(number, 0, -1):
                div *= n
            return (count // div)

        def calcDistinctPerms(hcount):
            #print(result)
            this_half = hcount
            the_other_half = len(num) - hcount
            total = 1
            for (number, count) in result:
                rem = numberCounts[number] - count
                if count > 0:
                    total = (total * getCount(this_half, count)) % MOD
                if rem > 0:
                    total = (total * getCount(the_other_half, rem)) % MOD
                this_half -= count
                the_other_half -= rem

            self.num_distinct_perms = (self.num_distinct_perms + total) % MOD

        
        @cache
        def findNumbersInHalf(which, sum_needed, odd_current, even_current):
            if which == -1:
                if sum_needed == 0 and odd_current == odd_count:
                    # calcDistinctPerms(odd_count)
                    return 1
                return 0
            if odd_current > odd_count:
                return 0
                    
            number = available_numbers[which]
            num_count = numberCounts[number]
            most_needed_count = num_count
            if number != 0:
                most_needed_count = (sum_needed +  number - 1) // number
                most_needed_count = min(most_needed_count, num_count)
            num_perms = 0
            odd_rem = odd_count - odd_current
            even_rem = even_count - even_current
            for c in range(most_needed_count, -1, -1):
                rem_sum = running_sum[number] - (num_count - c) * number
                if rem_sum < sum_needed:
                    continue

                remaining_sum = sum_needed - c * number
                
                ways = (getCount(odd_rem, c) *  getCount(even_rem, num_count - c)) % MOD
                #result.append((number, c))
                num_perms += (ways * findNumbersInHalf(which - 1, remaining_sum, c + odd_current, num_count - c + even_current))
                #result.pop()
            return num_perms % MOD

        perms = findNumbersInHalf(len(available_numbers) - 1, half_sum, 0, 0)
        print(self.num_distinct_perms)
        return(perms)

if __name__ == '__main__':
    s = Solution()
    #print(s.countBalancedPermutations('123'))
    #print(s.countBalancedPermutations('12345'))
    #print(s.countBalancedPermutations('112'))
    #print(s.countBalancedPermutations('33'))
    #print(s.countBalancedPermutations('022'))
    #print(s.countBalancedPermutations('86075'))
    #print(s.countBalancedPermutations('08143'))
    #print(s.countBalancedPermutations('18128'))
    #print(s.countBalancedPermutations('4567'))
    #print(s.countBalancedPermutations('98082883294315468135708651902526647108'))
    #print(s.countBalancedPermutations('15338359781342159844683188511637883821754570632088685'))
    #print(s.countBalancedPermutations('40709214682653206589154392873998729188911623044929529116'))
    print(s.countBalancedPermutations('580252396598107678405205488752871650118935293993424304629'))
