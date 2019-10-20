# 思路
"""
快慢指针，快指针记录前移删除元素，慢指针记录被删除元素的前一元素，
每次从重复元素的后面删除
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
        dummyhead = ListNode(None)

        dummyhead.next = head
        phead = head
        pre = dummyhead
        equal_flag = False
        while phead and phead.next:
            if phead.val == phead.next.val:
                phead.next = phead.next.next
                equal_flag = True
            else:
                if equal_flag:
                    pre.next = phead.next
                    phead = phead.next
                    if phead and phead.next and not phead.val == phead.next.val:
                        pre = phead
                    equal_flag = False
                else:
                    pre = phead
                    phead = phead.next

        if equal_flag:
            pre.next = phead.next

        return dummyhead.next



