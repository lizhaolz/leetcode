# 思路

"""

正向思维，
1. 先遍历两个链表，把两个链表分别变成两个字符串，然后反转字符串，并整数化对反转后的
   字符串，这样即得到两个真实的数字
2. 把第一步得到的两数相加，并字符串化，方便后面循环取出放入链表
3. 设置两个节点，一个哑节点dummyHead(头节点前的虚节点)，一个循环节点cur
   小技巧：
   对于链表问题，返回结果为头结点时，通常需要先初始化一个预先指针 dummyHead，该指针的下一个节点指向真正的头结点head。
   使用预先指针的目的在于链表初始化时无可用节点值，而且链表构造过程需要指针移动，进而会导致头指针丢失，无法返回结果。
4. 反向循环字符串，依次将每个字符整数化之后存入链表:
5. 返回哑节点的下一节点，即头节点

"""

# 代码

# Definition for singly-linked list.


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

        s1 = ''
        s2 = ''
        while l1:
            s1 = s1 + str(l1.val)
            l1 = l1.next
        num1 = int(s1[::-1])
        #print(num1)

        while l2:
            s2 = s2 + str(l2.val)
            l2 = l2.next
        num2 = int(s2[::-1])
        #print(num2)

        result = num1 + num2
        str_resu = str(result)

        dummyHead = ListNode(0)
        cur = dummyHead
        for x in str_resu[::-1]:
            cur.next = ListNode(x)
            cur = cur.next
            '''
            tmp_node.next = ListNode(int(x))
            tmp_node = tmp_node.next
            print('tmpnode', tmp_node.val)
            '''
        return dummyHead.next


if __name__ == '__main__':
    l1 = ListNode(2)
    tempnode = ListNode(4)
    tempnode1 = ListNode(3)
    l1.next = tempnode
    tempnode.next = tempnode1

    l2 = ListNode(5)
    tempnode2 = ListNode(6)
    tempnode3 = ListNode(4)
    l2.next = tempnode2
    tempnode2.next = tempnode3
    s = Solution()
    res = s.addTwoNumbers(l1, l2)
    while res:
        print(res.val)
        res = res.next
