# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
         if n == 0:
             return []

         def build(l, r):
             if l > r:
                 return [None]

             res = []
             for root in range(l, r + 1):
                 lefts = build(l, root - 1)
                 rights = build(root + 1, r)

                 for L in lefts:
                     for R in rights:
                         node = TreeNode(root)
                         node.left = L
                         node.right = R
                         res.append(node)

             return res

         return build(1, n)
