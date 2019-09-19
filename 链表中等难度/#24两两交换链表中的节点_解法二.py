# 思路
"""
递归
"""
# 代码


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        else:
            pre = head
            res = pre.next
            cur = head.next
            pcurnext = cur.next
            cur.next = pre
            pre.next = self.swapPairs(pcurnext)
            return res
