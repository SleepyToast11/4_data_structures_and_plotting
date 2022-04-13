import hashlib


class HTLP:

    class Node:
        __slots__ = 'key', 'value'

        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, size):
        self.table = [None] * size
        self.size = size
        self.values = 0

    class Del_Node: #placeholer node when delete happens that will always be ignored by when searching for element
        def __init__(self):
            self.key = -1

    def hash(self, key):
        return int((hashlib.md5(str(key).encode('ASCII')).hexdigest()), 16) % self.size  #Other simpler hash algo were to bad for use, so went with something more sure

    def __setitem__(self, key, value):
        if self.values == self.size:
            raise OverflowError
        else:
            self.values += 1
            temp = self.hash(key)
            while self.table[temp] is not None and type(self.table[temp]) is not self.Del_Node and self.table[temp].key != key:
                temp = (temp + 1) % self.size
            self.table[temp] = self.Node(key, value)


    def __len__(self):
        return self.values

    def __getitem__(self, key):
        hash = self.hash(key)
        while self.table[hash] is not None:
                if self.table[hash].key == key:
                    return self.table[hash].value
                else:
                    hash += 1
        raise KeyError

    def __delitem__(self, key):
        hash = self.hash(key)
        while self.table[hash] is not None:
                if self.table[hash].key == key:
                    self.table[hash] = self.Del_Node()
                    self.values -= 1
                    return
                else:
                    hash += 1
        raise KeyError
