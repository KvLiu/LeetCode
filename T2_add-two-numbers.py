# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        re = r = ListNode(0)
        carry = 0 #carry进位数 0或1
        while (l1 or l2):
            if l1:
                x = l1.val
            else:
                x = 0
            if l2:
                y = l2.val
            else:
                y = 0
            s = carry + x + y
            r.next = ListNode(s%10)  #本节点保留个位数作为val
            r = r.next
            carry = s/10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry != 0:
            r.next = ListNode(1)

        return re.next


if __name__ == '__main__':
    print("test start...")
    l11 = ListNode(1)
    l12 = ListNode(3)
    l13 = ListNode(5)
    l11.next = l12
    l12.next = l13

    l21 = ListNode(3)
    l22 = ListNode(2)
    l23 = ListNode(1)
    l21.next = l22
    l22.next = l23

    a = Solution()
    print (a.addTwoNumbers(l11, l21))