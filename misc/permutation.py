def permutation(data, prefix):
    if data == []:
        print(prefix)
        return
    for i, v in enumerate(data):
        prefix.append(v)
        rem = data[:i] + data[i+1:]
        permutation(rem, prefix)
        prefix.pop()

#with duplicate
# permutation([1, 3, 3, 2,2], [1, 2, 3],  [])
def permutation(data, unique, prefix):
    if data == []:
        print(prefix)
        return
    used = {}
    for v in unique:
        used[v] = False
    for i, v in enumerate(data):
        if not used[v]:
            prefix.append(v)
            rem = data[:i] + data[i+1:]
            permutation(rem, unique, prefix)
            prefix.pop()
            used[v] = True

def getPerm(size, countMap, prefix):
    if size == 0:
        print(prefix)
        return
    for key, count in countMap.items():
        if count > 0:
            countMap[key] -= 1
            prefix.append(key)
            getPerm(size - 1, countMap, prefix)
            prefix.pop()
            countMap[key] = count
            
    
def permutation(data):
    countMap = {}
    for v in data:
        countMap[v] = countMap[v] + 1 if v in countMap else 1
    print(countMap)
    getPerm(len(data), countMap, [])
