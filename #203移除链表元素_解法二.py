# 思路
"""
递归
对head.next执行移除操作，之后判断head是否为要删除的元素。
递归的思想是对子链执行同样的操作，并且要确定递归的结束条件
"""

# 代码


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        if head is None:
            return None
        elif head.val == val:
            return self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
            return head


if __name__  == "__main__":
    l = [2, 6, 3, 4, 5, 6]
    head = ListNode(1)
    temp = head
    for i in l:
        temp.next = ListNode(i)
        temp = temp.next

    s = Solution()
    val = 6
    res = s.removeElements(head, val)
    while res:
        print(res.val)
        res = res.next

