def _checkBST(root):
    if root is None:
        return []
    left_items = _checkBST(root.left)
    if root.left:
        if not left_items or root.data <= left_items[-1]:
            return []
    right_items = _checkBST(root.right)
    if root.right:
        if not right_items or root.data >= right_items[0]: 
            return []
    return left_items + [root.data] + right_items
    

def checkBST(root):
    result = _checkBST(root)
    return result != []
