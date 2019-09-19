# 思路
"""
常规解法
设置三个节点，一个指向前一节点，一个指向当前节点，一个保存当前节点的下一节点
遍历，当前节点的值指向前一节点。判断当前节点的下一节点及下下个节点是否为空，
若不为空，前一节点指向当前节点的下一节点，改变当前节点和前一节点的位置继续遍历。
若为空，则代表遍历到只剩下一个节点或者没有剩下节点，将前一节点指向当前节点的下一节点，
跳出遍历。
注意保存原来的头节点的下一个节点，即交换后链表的头节点，这是返回值，
不能直接返回头节点的下一节点，因为反转后的头节点变了
（头节点现在是第二个节点，他的下一个节点是第三个节点）。
注意判断链表为空或者只有一个节点
"""
# 代码


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        # 空链表或者只有一个节点
        if head is None or head.next is None:
            return head

        else:
            pre = head
            cur = head.next
            # res为头节点的下一节点，即现在链表的头节点
            res = cur
            while True:
                pcurnext = cur.next
                cur.next = pre
                if pcurnext and pcurnext.next:
                    pre.next = pcurnext.next
                    pre = pcurnext
                    cur = pcurnext.next
                else:
                    pre.next = pcurnext
                    break

            return res

