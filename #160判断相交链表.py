# 思路
"""
常规解法
对一个链表的每个节点，遍历另一个链表，看是否出现，若出现
则相交，否则，不相交
时间复杂度：O（m*n）
空间复杂度：O(1)
"""
# 代码


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        else:
            curA = headA
            while curA:
                curB = headB
                while curB:
                    if curA == curB:
                        return curA
                    else:
                        curB = curB.next
                curA = curA.next
        return None


if __name__ == "__main__":

    headA = ListNode(4)
    temp = headA
    temp.next = ListNode(1)
    temp = temp.next
    temp.next = ListNode(8)
    IntersectionNode = temp.next
    temp = temp.next
    temp.next = ListNode(4)
    temp = temp.next
    temp.next = ListNode(5)

    headB = ListNode(5)
    tempB = headB
    tempB.next = ListNode(0)
    tempB = tempB.next
    tempB.next = ListNode(1)
    tempB = tempB.next
    tempB.next = IntersectionNode

    s = Solution()
    res = s.getIntersectionNode(headA, headB)
    if res:
        print(res.val)
    else:
        print('Null')
