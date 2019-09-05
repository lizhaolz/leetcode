# 思路
"""
常规解法
1.先构造一个带哑节点dummyHead的新的链表
2.遍历l1和l2，判断哪个节点存的数字小，将其插入新链表，直到一个链表全部插入到新链表
3.将未遍历完的链表直接插入到新链表尾部
4.返回头节点,即dummyHead.next
"""
# 代码


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        cur = dummyHead
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next

        if l1:
            cur.next = l1

        if l2:
            cur.next = l2

        return dummyHead.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    c = Solution()
    result = c.mergeTwoLists(l1, l2)
    while result:
        print(result.val)
        result = result.next



