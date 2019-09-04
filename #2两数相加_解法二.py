# 思路
"""
1. 先以长度较小的一条链为基准，将两条链节点数相加，并将结果存在链表中，
   每一位计算需要考虑上一位的进位问题，而当前计算结束后同样需要更新进位，
   计算第一位时，将上一位的进位看作零。每次进位为sum//10,结果为sum%10
2. 分别遍历完l1或l2剩余的数，注意还要加上一步的进位
3. 若两条链全部遍历完后，进位值为1，则在新链表最前方添加节点1
4. 返回哑节点dummyHead的下一节点，即头节点
   小技巧：对于链表问题，返回结果为头结点时，通常需要先初始化一个预先指针 pre，
   该指针的下一个节点指向真正的头结点head。使用预先指针的目的在于链表初始化时无可用节点值，
   而且链表构造过程需要指针移动，进而会导致头指针丢失，无法返回结果。
"""

# 代码


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0  # 进位
        dummyHead = ListNode(0)  # 哑节点
        cur = dummyHead  # 循环节点
        while l1 and l2:
            sum = l1.val + l2.val + carry  # 计算时要考虑上一位进位
            carry = sum // 10  # 计算后重新更新进位值
            cur.next = ListNode(sum % 10)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum = l1.val + carry
            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
            l1 = l1.next

        while l2:
            sum = l2.val + carry
            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
            l2 = l2.next

        if carry == 1:
            cur.next = ListNode(1)

        return dummyHead .next

if __name__ == '__main__':
    l1 = ListNode(2)
    tempnode = ListNode(4)
    tempnode1 = ListNode(3)
    l1.next = tempnode
    tempnode.next = tempnode1
    print(len(l1))

    l2 = ListNode(5)
    tempnode2 = ListNode(6)
    tempnode3 = ListNode(4)
    l2.next = tempnode2
    tempnode2.next = tempnode3
    s = Solution()
    res = s.addTwoNumbers(l1, l2)
    print(res)
