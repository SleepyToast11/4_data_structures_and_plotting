class BNS:
    class Node:
        __slots__ = 'key', 'parent', 'left', 'right', 'value'

        def __init__(self, key, parent, left, right):
            self.key = key
            self.parent = parent
            self.left = left
            self.right = right
            self.value = None

    root = Node(3, None, None, None)
    size = 4
    values = 0

    def __setitem__(self, key, value):
        self.values += 1
        while self.size < key:
            self.increase_size()
        self.search_key(key, self.root).value = value

    def __len__(self):
        return self.values

    def __getitem__(self, key):
        temp = self.search_key(key, self.root)
        if temp.value is None:
            raise KeyError
        else:
            return temp.value

    def increase_size(self):
        new_root = self.Node(self.size + 1, None, self.root, None)
        difference = self.size * 2 - self.size
        new_root.right = self.Node(self.root.key + difference, new_root, None, None)
        self.create_node(self.root, new_root.right, difference)
        self.size *= 2
        self.root = new_root

    def search_key(self, key, node):
        if node.key == key:
            return node
        else:
            if node.key < key:
                return self.search_key(key, node.right)
            else:
                return self.search_key(key, node.left)

    def create_node(self, old_node, new, difference):
        if old_node.right is None:
            return
        else:
            new.right = self.Node(old_node.right.key + self.size, new, None, None)
            new.left = self.Node(old_node.left.key + self.size, new, None, None)
            self.create_node(old_node.right, new.right, difference)
            self.create_node(old_node.left, new.left, difference)

    def __delitem__(self, key):
        temp = self.search_key(key, self.root)
        if temp.value is None:
            raise KeyError
        else:
            temp.value = None
            self.values -= 1

    def sanitize(self):  # not tested yet
        while self.root.value is None and self.size > 4:
            if self.check_sanitize(self.root.right):
                temp = self.root
                self.root = temp.left
                self.root.parent = None
                self.size /= 2

    def check_sanitize(self, node):
        if node.value is not None:
            return False
        elif node.right is not None:
            return self.check_sanitize(node.right) and self.check_sanitize(node.left)
        else:
            return True

    def __init__(self):
        self.root.right = self.Node(4, self.root, None, None)
        self.root.left = self.Node(2, self.root, None, None)
        self.root.left.left = self.Node(1, self.root.left, None, None)
