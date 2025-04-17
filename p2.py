class ListNode:
    def __init__(self, key=None,data = None):
        self.key = key
        self.data = data
        self.next = self
        self.prev = self

class LRUCache:

    def __init__(self, capacity: int):
        self.hash_t = dict()
        self.cap = capacity
        self.size = 0
        self.stk = ListNode()

    def get(self, key: int) -> int:
        pass
        if key not in self.hash_t.keys():
            return -1
        else:
            self.move_to_head(key)
            return self.hash_t[key].data
        
    def put(self, key: int, value: int) -> None:
        # pass
        if key in self.hash_t.keys():
            # pass
            self.hash_t[key].data = value
            self.move_to_head(key)
        else:
            if self.size < self.cap:
                self.size = self.size+1
            else:
                tgt = self.stk.prev
                tgt.next.prev = tgt.prev
                tgt.prev.next = tgt.next
                del self.hash_t[tgt.key]
                
            new = ListNode(key, value)
            new.next = self.stk.next
            new.prev = self.stk

            self.stk.next.prev = new
            self.stk.next = new
            
            self.hash_t[key] = new
            
            
    def move_to_head(self, key):
        cur = self.hash_t[key]
        prev = cur.prev
        next = cur.next
        prev.next = next
        next.prev = prev

        cur.next = self.stk.next
        cur.prev = self.stk
        self.stk.next.prev = cur
        self.stk.next = cur
        

        


        

lRUCache = LRUCache(2)
lRUCache.put(1, 1) 
lRUCache.put(2, 2) 
print(lRUCache.get(1)    )
lRUCache.put(3, 3) 
print(lRUCache.get(2)    )
lRUCache.put(4, 4) 
print(lRUCache.get(1)    )
print(lRUCache.get(3)    )
print(lRUCache.get(4)    )

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)