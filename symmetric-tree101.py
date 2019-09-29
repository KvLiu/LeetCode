# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import TreeNode
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        else:
            return self.is_Symmetric(root.left,root.right)

    def is_Symmetric(self, l, r):
        if not l and not r:
            return True
        if not (l and r):
            return False
        if l.val != r.val:
            return False
        else:
            return self.is_Symmetric(l.left, r.right) and \
                   self.is_Symmetric(l.right, r.left)


