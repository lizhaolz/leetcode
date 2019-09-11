# 思路
"""
按照常规思路来做，分以下几种情况
1. 常规情况：A链表和B链表至少都有一个节点
   先遍历一遍，得到两链表的长度，之后先让长的链表走到两个长度相等的地方
   之后两个链表从长度开始的地方一起走，如果相交，返回交点，
   如果不相交，则同时返回Null。
2. 链表头相等，任意返回一个
3. A链只有一个节点，B链为空，且headA.next == headB，返回headB
4. 一个是另一个子链，解法同情况一
"""
# 代码
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA == headB:  # 情况2
            return headA
        if headA and headA.next == headB:  # 情况3
            return headB
        if headB and headB.next == headA:  # 情况3
            return headA
        # 情况1
        lengthA = 0
        curA = headA
        while curA:
            lengthA = lengthA + 1
            curA = curA.next

        lengthB = 0
        curB = headB
        while curB:
            lengthB = lengthB + 1
            curB = curB.next

        difference = (lengthB - lengthA) if lengthB > lengthA else (lengthA - lengthB)
        temp = 0
        curA = headA
        curB = headB
        while temp < difference:
            if lengthB > lengthA:
                curB = curB.next
            else:
                curA = curA.next
            temp = temp + 1

        while curA and curB:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next


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
        print(res)



