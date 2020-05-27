def run(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return run(n-1) + run(n-2) + run(n-3)
