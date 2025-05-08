def insertNodeAtPosition(llist, data, position):
    next = prev = llist
    node = SinglyLinkedListNode(data)
    if llist is None:
        return node
    else:
        for i in range(position):
            prev = next
            next = next.next
        prev.next = node
        node.next = next
        return llist
