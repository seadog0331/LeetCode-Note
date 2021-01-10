class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = collections.OrderedDict()

    def get(self, key):
        if key not in self.queue:
            return -1
        value = self.queue.pop(key)
        self.queue[key] = value
        return self.queue[key]
    
    def put(self, key, value):
        if key in self.queue:
            self.queue.pop(key)
        elif len(self.queue.items()) == self.capacity:
            self.queue.popitem(last=False) 
            # OrderedDict.popitem()有一个可选参数last（默认为True），当last为True时它从OrderedDict中删除最后一个键值对并返回该键值对，当last为False时它从OrderedDict中删除第一个键值对并返回该键值对。
        self.queue[key] = value
