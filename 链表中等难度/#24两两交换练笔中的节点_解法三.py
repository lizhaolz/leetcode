#思路
"""
常规解法
添加哑头节点，之后再按照常规解法
"""
# 代码


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        dummyhead = ListNode(-1)
        dummyhead.next = head
        pa = dummyhead
        while pa.next and pa.next.next:
            pb = pa.next
            pc = pa.next.next
            pa = pc
            pb = pc.next
            pc.next = pb

            pa = pa.next.next
        return dummyhead.next
