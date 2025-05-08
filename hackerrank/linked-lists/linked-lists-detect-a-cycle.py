def has_cycle(head):
    p1 = head
    p2 = head.next
    while p2:
        p1 = p1.next
        p2 = p2.next
        if p2 == p1:
            return True
        if p2:
            p2 = p2.next
    return False
