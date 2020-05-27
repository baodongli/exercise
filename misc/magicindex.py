// data in asending order and unique
def magic_index(data, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if data[mid] == mid:
        return mid
    if data[mid] > mid:
        return magic_index(data, start, mid - 1)
    else:
        return magic_index(data, mid + 1, end)

// data in asending order but not unique
def magic_index2(data, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    if data[mid] == mid:
        print(mid)
        return
    left = min(data[mid], mid - 1)
    magic_index2(data, start, left)
    right = max(data[mid], mid + 1)
    magic_index2(data, right, end)
