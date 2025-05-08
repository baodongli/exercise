def sortedInsert(llist, data):
    # Write your code here
    node = DoublyLinkedListNode(data)
    p = llist
    prev = None
    while p and p.data < data:
        prev = p
        p = p.next
    # Insert at the tail
    if p is None:
        prev.next = node
        node.prev = prev
        return llist
    
    # Insert at the head
    if p == llist:
        node.next = p
        p.prev = node
        return node
    
    # Insert in between
    node.prev = prev
    prev.next = node
    node.next = p
    p.prev = node
    return llist
