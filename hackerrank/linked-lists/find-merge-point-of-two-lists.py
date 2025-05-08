def findMergeNode(head1, head2):
    size1 = size2 = 0
    list1 = head1
    list2 = head2
    while list1 is not None:
        size1 += 1
        list1 = list1.next
    while list2 is not None:
        size2 += 1
        list2 = list2.next
    
    start1 = head1
    start2 = head2
    if size1 > size2:
        for i in range (size1 - size2):
            start1 = start1.next
    if size1 < size2:
        for i in range(size2 - size1):
            start2 = start2.next
    while start1 != start2:
        start1 = start1.next
        start2 = start2.next
    if start1:
        return start1.dat
