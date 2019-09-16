# 思路
"""
递归
对头节点的下一个节点的子链执行反转操作，
之后遍历反转后的子链到尾部，将头节点插入到尾部。
递归结束条件为头节点为空（链表为空）或者
头节点的下一个节点为空（只有一个节点）
"""
# 代码


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        else:
            last = self.reverseList(head.next)
            cur = last
            while cur.next:
                cur = cur.next
            cur.next = head
            head.next = None
            return last


if __name__ == "__main__":
    head = ListNode(1)
    temp = head
    for i in range(2, 6):
        temp.next = ListNode(i)
        temp = temp.next
    s = Solution()
    res = s.reverseList(head)
    while res:
        print(res.val)
        res = res.next
