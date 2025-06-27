# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, vkl=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def genTrees(left, right):
            if left > right:
                return [None]
            if left == right:
                return [TreeNode(left)]

            trees = [] 
            for i in range(left, right+1):
                leftTree = genTrees(left, i - 1)
                rightTree = genTrees(i+1, right)
                for l in leftTree:
                    for r in rightTree:
                        trees.append(TreeNode(i, l, r))
            return trees
            
        return genTrees(1, n)
