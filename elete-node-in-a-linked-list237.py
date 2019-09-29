#https://leetcode-cn.com/problems/delete-node-in-a-linked-list/submissions/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        next_next_node = node.next.next
        node.val = next_node.val
