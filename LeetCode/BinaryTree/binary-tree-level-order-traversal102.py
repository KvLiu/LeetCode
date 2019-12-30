#https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        cur_nodes = [root]
        next_nodes = []
        res.append([i.val for i in cur_nodes])
        while cur_nodes:
            for i in cur_nodes:
                if i.left:
                    next_nodes.append(i.left)
                if i.right:
                    next_nodes.append(i.right)
            if next_nodes:
                res.append([i.val for i in next_nodes])
            cur_nodes = next_nodes
            next_nodes = []

        return res




















