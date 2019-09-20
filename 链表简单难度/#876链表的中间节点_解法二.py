# 思路
"""
常规解法
先遍历求长度，再求中点
"""
# 代码


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        if head.next is None:
            return head
        else:
            length = 0
            phead = head
            while phead:
                length += 1
                phead = phead.next
            middle = length // 2 + 1

            pmiddle = head
            temp = 1
            while temp < middle:
                pmiddle = pmiddle.next
                temp += 1
            return pmiddle
