class LRUCache:

    def __init__(self, capacity: int):
        self.LRU = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.LRU:
            value, prev, next = self.LRU[key]

            if next is not None:
                self.LRU[next][1] = prev
                if prev is not None: 
                    self.LRU[prev][2] = next
                elif prev is None: 
                    self.head = next

                self.LRU[key] = [value, self.tail, None]
                if self.tail is not None:
                    self.LRU[self.tail][2] = key

            self.tail = key
            return value

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.LRU:
            _, prev, next = self.LRU[key]

            if next is None:
                self.LRU[key][0] = value
            else:
                self.LRU[next][1] = prev
                if prev is not None: 
                    self.LRU[prev][2] = next
                elif prev is None: 
                    self.head = next

                self.LRU[key] = [value, self.tail, None]
                if self.tail is not None:
                    self.LRU[self.tail][2] = key

        elif len(self.LRU) == self.capacity:
                next = self.LRU[self.head][2]
                del self.LRU[self.head]
                if next is not None:
                    self.head = next
                    self.LRU[self.head][1] = None

                    self.LRU[key] = [value, self.tail, None]
                    if self.tail is not None:
                        self.LRU[self.tail][2] = key
                elif next is None: 
                    self.head = key
                    self.LRU[key] = [value, None, None]

        else:
            if self.head is None:
                self.head = key

            self.LRU[key] = [value, self.tail, None]
            if self.tail is not None:
                self.LRU[self.tail][2] = key

        self.tail = key