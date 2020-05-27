import copy
def get_all_subset(data):
    if data == set():
        return [set()]
    elem = data.pop()
    subsets = get_all_subset(data)
    result = copy.deepcopy(subsets)
    for s in subsets:
        s.add(elem)
        result.append(s)
    return result
