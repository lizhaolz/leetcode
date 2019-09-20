# 思路
"""
如果两个链表相交，那么交点距离链表尾部的距离相等，
如果让两个链表从距离尾部等距离的地方开始遍历（短链表的头节点），
若相交，则一定可以同时到达交点，若不相交，则同时到达None
那么怎么让他们从距离末尾等距的地方开始呢，
让headA和headB同时开始遍历，若headA到达None，则headA指向链表B，若headB到达None，
则headB指向链表A，继续遍历，这样短链的指针就比长链的指针多走两条链表相差的长度，
两个指针最终会从距尾部等距离的地方开始遍历，继续遍历，直至两个指针相等，就找到了交点或者None
"""
# 代码

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        #  有一条链表为空
        if headB is None or headA is None:
            return None

        else:
            curA = headA
            curB = headB
            while curA != curB:
                if curA is None:
                    curA = headB
                elif curB is None:
                    curB = headA
                else:
                    curA = curA.next
                    curB = curB.next
            return curA


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




