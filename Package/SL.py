import random


class SL:
    class Node:
        __slots__ = 'left', 'right', 'down', 'up', 'key', 'value'
        def __init__(self, left, right, up, key, value):
            self.left = left
            self.right = right
            self.down = None
            self.up = up
            self.key = key
            self.value = value

    class Heads:
        __slots__ = 'right', 'down', 'up'
        def __init__(self, down):
            self.right = None
            self.down = down
            self.up = None

    def __init__(self):
        self.head = self.Heads(None)
        self.height = 0
        self.values = 0


    def get_top_head(self):
        head = self.head
        while head.up is not None:
            head = head.up
        return head

    def determine_height(self):
        sum = 0
        while random.randint(0,99) <= 50:
            sum += 1
        sum = 2
        if sum > self.height:
            top = self.get_top_head()
            while sum != self.height:
                top.up = self.Heads(top)
                top = top.up
                self.height += 1
        return sum

    def del_node(self, node):
        if node.right is None:
            if type(node.left) is self.Heads:
                node.left = None
            else:
                node = None
        else:
            node.right.left = node.left
            node.left.right = node.right

    def __delitem__(self, key):
        node = self.get_top_head()
        height = self.height
        while height >= 0:
            while self.check_next(node, key):
                if node.right.key == key:
                    node = node.right
                    while height >= 0:
                        self.del_node(node)
                        if node.down is not None:
                            node = node.down
                            node.up = None
                        else:
                            node = None
                        height -= 1
                    self.values -= 1
                    return
                node = node.right
            if node.down is not None:
                node = node.down
            height -= 1
        raise KeyError

    def key_exist(self, key):
        node = self.get_top_head()
        height = self.height
        while height >= 0:
            while self.check_next(node, key):
                if node.right.key == key:
                    return True
                node = node.right
            if node.down is not None:
                node = node.down
            height -= 1
        return False


    def check_next(self, node, key):
        if type(node) is self.Heads:
            if node.right is not None:
                return node.right.key <= key
            else:
                return False
        elif node.right is not None:
            return node.right.key <= key
        else:
            return False


    def __setitem__(self, key, value):
        if self.key_exist(key):     #if key already exists, delete then overwrite
            self.__delitem__(key)
        self.values += 1
        last = None
        sum = self.determine_height()
        head = self.get_top_head()
        while sum >= 0:
            while self.check_next(head, key):
                head = head.right
            if head.right is None:
                head.right = self.Node(head, None, last, key, value)
                if last is not None:
                    last.down = head.right
                last = head.right
            else:
                head.right.left = self.Node(head, head.right, last, key, value)
                head.right = head.right.left
                if last is not None:
                    last.down = head.right
                last = head.right
            if head.down is not None:
                head = head.down
            sum -= 1

    def __getitem__(self, key):
        node = self.get_top_head()
        height = self.height
        while height >= 0:
            while self.check_next(node, key):
                if node.right.key == key:
                    return node.right.value
                node = node.right
            if node.down is not None:
                node = node.down
            height -= 1
        raise KeyError