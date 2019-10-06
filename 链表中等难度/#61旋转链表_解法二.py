# 思路
"""
链表中的点已经存在，一次旋转操作意味着
1. 先将链表闭合成环
2. 找到相应位置断开环，确定链表新的头和尾

算法：
1. 找到旧的尾部并将其与链表头相连。old.tail.next = head , 整个链表形成闭环，同时计算出链表长度n
2. 找到新的头部，第n-k%n个节点。新的尾部，第n - k%n -1个节点
3. 断开环 new_tail.next = None，并返回新的链表头new_head
"""

# 代码

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        else:

            # 求长度，连环
            length = 0
            phead = head
            old_tail = phead
            while phead:
                length += 1
                old_tail = phead
                phead = phead.next
            old_tail.next = head
            k = k % length
            loop = 0

            # 找新的头和尾，断环
            temphead = head
            while loop < length - k - 1:
                temphead = temphead.next
                loop += 1

            new_head = temphead.next
            new_tail = temphead
            new_tail.next = None

            return new_head


