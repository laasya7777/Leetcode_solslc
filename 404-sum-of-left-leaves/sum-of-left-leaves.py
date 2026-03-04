# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def of(root, isLeft):
            if not root: return 0
            if not root.left and not root.right and isLeft: return root.val
            return of(root.left, True)+of(root.right, False)
        return of(root, False)
        