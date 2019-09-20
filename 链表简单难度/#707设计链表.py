# 节点

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 链表

class MyLinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    def get(self, index):
        print(self.length)
        if index < 0 or index > self.length - 1:
            print('xx')
            return -1
        else:
            temp = 0
            phead = self.head
            while temp < index:
                phead = phead.next
                temp += 1
            return phead.val

    def addAtHead(self, val):
        print('yym')
        temp = ListNode(val)
        temp.next = self.head
        self.head = temp
        self.length += 1
        print(self.length)
        print(self.head)

    def addAtTail(self, val):
        phead = self.head
        if phead is None:
            print('lz')
            self.addAtHead(val)
        else:
            while phead.next:
                phead = phead.next
            phead.next = ListNode(val)
            self.length += 1

    def addAtIndex(self, index, val):
        if index == self.length:
            print('a')
            self.addAtTail(val)
        elif index <= 0:
            print('b')
            self.addAtHead(val)
        elif 0 < index < self.length:
            print('c')
            phead = self.head
            temp = 0
            while temp < index - 1:
                phead = phead.next
                temp += 1

            ptemp = phead.next
            phead.next = ListNode(val)
            phead.next.next = ptemp
            self.length += 1

    def deleteAtIndex(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -= 1
        elif 0 < index < self.length:
            temp = 0
            phead = self.head
            while temp < index - 1:
                phead = phead.next
                temp += 1

            phead.next = phead.next.next
            self.length -= 1


if __name__ == "__main__":
    l = MyLinkedList()
    #c = l.get(0)
    #print('c', c)
    #l.addAtIndex(1, 2)
    #d = l.get(0)
    #print('d', d)
    #e = l.get(1)
    #print('e', e)
    l.addAtIndex(0, 1)
    #f = l.get(0)
    #print('f', f)
    res = l.get(1)

    print(res)
