def get_combination(start, total, sample, prefix):
    if sample == 0:
        print(prefix)
        return
    for p in range(start, total - sample + 1):
        prefix.append(p+1)
        get_combination(p+1, total, sample - 1, prefix)
        prefix.pop()
