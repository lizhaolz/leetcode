# 我要怎么保存他分割的每个链表，总不能给每个链表加一个头，
# 加头我也没法加啊
"""
所以，可以从底至顶直接合并,而不是先把八个分四个，四个分两个，
是直接把他们认为是单独的一个，然后两两合并,设intv为要合并的大小，
则intv = 1，2，4，8.当intv大于链表长度时，则代表合并完成。
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = head
        length = 0
        intv = 1
        while h:
            h = h.next
            length += 1
        res = ListNode(0)
        res.next = head
        # merge the list in different intv
        while intv < length:
            pre = res
            h = res.next
            while h:
                # get the two merge head 'h1'and 'h2'
                h1 = h
                count = intv
                while count and h:
                    h = h.next
                    count = count-1
                # count还没减到0，即还没走到好h2，h就不存在了，
                # 则代表h2不存在，这样的话，不需要合并，直接跳出
                if count:
                    break
                h2 = h
                count = intv
                # h2 存在，但是长度比intv小
                while count and h:
                    h = h.next
                    count = count - 1
                # c1,c2分别代表h1,h2的长度
                c1 = intv
                c2 = intv - count
                # 合并h1,h2, 这块跟数组的思想一样，
                # 把pre看作新链表的头
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next = h1
                        h1 = h1.next
                        c1 = c1 - 1
                    else:
                        # 这时候不直接把h1插到h2后面，
                        # 而是跟数组一样， 把pre当作新的链表，
                        # 直接把h2插到pre后面
                        # 自己想的时候没有理解这个怎么插
                        pre.next = h2
                        h2 = h2.next
                        c2 = c2 - 1

                    pre = pre.next
                if c1:
                    pre.next = h1
                else:
                    pre.next = h2
                # 但是上一步执行完并没有把pre
                # 移到排好序部分的链表的尾部
                while c1 > 0 or c2 > 0:
                    pre = pre.next
                    c1 = c1 - 1
                    c2 = c2 - 1
                # 如果最后是h1插入到pre,就算你把pre指向h1的尾部
                # 但是h1尾部的下一个元素是指向已经排好序的h2
                # 所以要把pre指向还未排序的h2尾部的下一个元素，即h
                pre.next = h
            intv *= 2
        return res.next


