import random
lower = 11
upper = 65535

print("Prime numbers between", lower, "and", upper, "are:")

primes = []
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           primes.append(num)

for p in random.sample(primes, 300):
    print(f"  - {p}")
