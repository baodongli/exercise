# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        def recover(root, res):
            if root is None:
                return None, None, []
            lminnode, lmaxnode, left_bad = recover(root.left, res)
            found = False
            left = None
            right = None
            if lmaxnode is not None and root.val < lmaxnode.val:
                left = lmaxnode
                found = True
            
            rminnode, rmaxnode, right_bad = recover(root.right, res)
            if rminnode is not None and root.val > rminnode.val:
                right = rminnode
                found = True

            if found:
                if right_bad:
                    rn, rl, rr = right_bad[-1]
                    index = 1
                    if rl:
                        index += 1
                    if rr:
                        index += 1
                    res.insert(-index, root)
                    if right is not None and right != rn:
                        res.insert(-index, right)
                else:
                    res.append(root)
                    if right is not None:
                        res.append(right)

                idx = res.index(root)
                if left_bad:
                    ln, ll, lr = left_bad[-1]
                    if left is not None:
                        if left != ln:
                            res.insert(idx, left)
                elif left is not None:
                    res.insert(idx, left)
                            
                return root, root, left_bad + [(root, left, right)] + right_bad
            minnode = None
            maxnode = None
            if lminnode is not None and lminnode.val < root.val:
                minnode = lminnode
            else:
                minnode = root
            if rmaxnode is not None and root.val < rmaxnode.val:
                maxnode = rmaxnode
            else:
                maxnode = root
                
            return minnode, maxnode, left_bad + right_bad 

        res = [TreeNode(-math.inf)]
        _, _, bad_nodes = recover(root, res)
        res.append(TreeNode(math.inf))

        first = None
        second = None
        for i in range(1, len(res)+1):
            if not first:
                if res[i].val < res[i-1].val:
                    first = res[i - 1]
            else:
                if res[i].val > first.val:
                    second = res[i - 1]
                    break
        first.val, second.val = second.val, first.val
        '''
        def inOrderTraversal(root, res):
            if root is None:
                return
            inOrderTraversal(root.left, res)
            res.append(root)
            inOrderTraversal(root.right, res)
        res = [TreeNode(-math.inf)]
        inOrderTraversal(root, res)
        res.append(TreeNode(math.inf))
        first = None
        second = None
        for i in range(1, len(res)+1):
            if not first:
                if res[i].val < res[i-1].val:
                    first = res[i - 1]
            else:
                if res[i].val > first.val:
                    second = res[i - 1]
                    break
        first.val, second.val = second.val, first.val
        
