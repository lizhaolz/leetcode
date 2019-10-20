# 思路
"""
还是快慢指针法， 这次从重复元素的最前面一个开始删除，
tips：加哑节点
注意慢指针的移动
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
        equal_flag = False
        dummyhead = ListNode(None)
        dummyhead.next = head
        pre = dummyhead
        phead = head
        while phead and phead.next:
            if phead.val == phead.next.val:
                pre.next = phead.next
                equal_flag = True
            else:
                if equal_flag:
                    pre.next = phead.next
                    if phead.next.next and not phead.next.next.val == phead.next.val:
                        pre = phead.next
                    equal_flag = False
                else:
                    pre = phead
            phead = phead.next

        if equal_flag:
            pre.next = phead.next

        return dummyhead.next


