"""
思路，将奇节点放在一个链表里，偶链表放在另一个链表里。然后把偶链表接在奇链表的尾部
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        odd = head  # 奇链表的头
        even = head.next  # 偶链表的循环指针
        evenhead = even  # 偶链表的头
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return head

if __name__ == '__main__':

    head = ListNode(2)
    head.next = ListNode(1)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(6)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(7)
    s = Solution()
    res = s.oddEvenList(head)
    while res:
        print(res.val)
        res = res.next
