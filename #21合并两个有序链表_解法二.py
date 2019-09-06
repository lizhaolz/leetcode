# 思路
"""
递归法
1. 如下定义两个链表的merge操作(忽略边界情况，比如空链表)
   list1[0]+merge(list1[1:],list2) list1[0]<list2[0]
   list2[0]+merge(list1,list2[1:]) otherwise
   也就是说，两个链表头部较小的一个与剩下元素的merge操作结果合并
2. 考虑边界情况，如果l1或l2一开始就为空，则直接返回非空链表即可，
   否则，应判读l1和l2哪个头元素更小，然后递归地决定下一个添加到结果里的值
   若两链表都为空，则递归结束。
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

        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


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
