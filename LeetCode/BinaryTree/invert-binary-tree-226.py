# https://leetcode-cn.com/problems/invert-binary-tree/
class TreeNode(object):
    def __int__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = root.left, root.right
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root