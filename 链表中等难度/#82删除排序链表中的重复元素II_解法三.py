# 思路
"""
递归
终止条件，链表为空或者只有一个元素
若头为重复元素，则从第一个非重复元素递归
若头为非重复元素，则从重复元素的前一个非重复元素开始递归
"""

# 代码


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        else:
            phead = head
            if phead.val == phead.next.val:
                while phead and phead.next and phead.val == phead.next.val:
                    phead = phead.next
                return self.deleteDuplicates(phead.next)
            else:
                pre = phead
                while phead and phead.next and not phead.val == phead.next.val:
                    pre = phead
                    phead = phead.next
                pre.next = self.deleteDuplicates(phead)
                return head
