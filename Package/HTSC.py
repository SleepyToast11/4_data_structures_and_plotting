import hashlib

class HTSC:
    class Bucket_Node:
        __slots__ = 'key', 'value', 'prev', 'next'

        def __init__(self, key, value, prev):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = None

    values = 0

    def hash(self, key):
        return int((hashlib.md5(str(key).encode('ASCII')).hexdigest()), 16) % self.size  #Other simpler hash algo were to bad for use, so went with something more sure

    def __init__(self, size):
        self.heads = [None] * size
        self.size = size

    def __setitem__(self, key, value):
        hashed_key = hash(key)
        node = self.heads[hashed_key]
        self.find_bucket(node, key, 0).value = value


    # opt if no node found: 0 returns a newly created node, else returns none
    def find_bucket(self, bucket, key, opt):
        if bucket is None: #will only happen if this is first time happening
            if opt == 0:
                self.heads[hash(key)] = self.Bucket_Node(key, None, bucket)
                return self.heads[hash(key)]
                self.size += 1
        if bucket.key is key:
            return bucket
        else:
            return self.find_bucket(bucket.next, key, 0)

    def __getitem__(self, key):
        hashed_key = hash(key)
        node = self.heads[hashed_key]
        if node is None:
            raise KeyError
        else:
            bucket = self.find_bucket(node, key, 1)
            if bucket is None:
                raise KeyError
            else:
                return bucket.value

    def __delitem__(self, key):
        hashed_key = hash(key)
        node = self.heads[hashed_key]
        if node is None:
            raise KeyError
        else:
            bucket = self.find_bucket(node, key, 1)
            if bucket is None:
                raise KeyError
            if bucket.prev is not None and bucket.next is not None:
                bucket.prev.next = bucket.next
                bucket.next.prev = bucket.prev
                bucket = None
            elif bucket.prev is None and bucket.next is None:
                self.heads[hashed_key] = None
            elif bucket.prev is None and bucket.next is not None:
                self.heads[hashed_key] = bucket.next
                bucket = None
            else:
                bucket = None
            return
            node = node.next
        raise KeyError

    def __len__(self):
        return self.values
