import sys

def rotate(v):
    v1 = v
    while True:
        q, r = divmod(v1, 10)
        v1 = 0
        m = 10
        while q != 0:
           v1 +=  r * m 
           m *= 10
           q, r = divmod(q, 10)
        v1 += r
        print(v1)
        if v1 == v:
            break

def rotate1(v):
    def left_one(v, d):
        q, r = divmod(v, d)
        return r * 10 + q
    min10s = 1
    q = v
    while True:
        q, r = divmod(q, 10)
        if q == 0:
            break
        min10s *= 10
    v1 = v
    while True:
        v1 = left_one(v1, min10s)
        print(v1)
        if v1 == v:
            break

if __name__ == "__main__":
    v = int(sys.argv[1])
    rotate(v)
    print("\n\n")
    rotate1(v)



