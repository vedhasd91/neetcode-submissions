class ListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}

        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1

        node = self.node_map[key]
        self.remove(node)
        self.add(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            self.remove(self.node_map[key])

        node = ListNode(key,value)
        self.node_map[key] = node    
        self.add(node)

        if len(self.node_map) > self.capacity:
            del self.node_map[self.head.next.key]
            self.remove(self.head.next)

        

    def add(self, node):
        prev_node = self.tail.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev
