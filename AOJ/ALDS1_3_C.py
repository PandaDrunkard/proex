class Node(object):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList(object):

    def __init__(self):
        self.dummy = Node(None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def insert(self, x):
        node = Node(x, self.dummy.next, self.dummy)

        self.dummy.next.prev = node
        self.dummy.next = node
    
    def delete(self, x):
        node = self.dummy.next
        while node != self.dummy:
            if node.value == x:
                self.__remove_node(node)
                break
            else:
                node = node.next
    
    def deleteFirst(self):
        self.__remove_node(self.dummy.next)

    def deleteLast(self):
        self.__remove_node(self.dummy.prev)

    def __remove_node(self, node):
        if node != self.dummy:
            node.prev.next = node.next
            node.next.prev = node.prev

    def items(self):
        ret = []
        node = self.dummy.next
        while node != self.dummy:
            ret.append(node.value)
            node = node.next
        return ret

def main():
    from sys import stdin
    store = LinkedList()
    for i in range(int(input())):
        parts = stdin.readline().strip().split()
        cmd = parts[0]
        if cmd == 'insert':
            store.insert(parts[1])
        elif cmd == 'delete':
            store.delete(parts[1])
        elif cmd == 'deleteFirst':
            store.deleteFirst()
        elif cmd =='deleteLast':
            store.deleteLast()

    print(' '.join(store.items()))

if __name__ == '__main__':
    main()
