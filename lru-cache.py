import functools

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.store = {}
        self.order = []
        self.size = 0
        self.capacity = capacity
        

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.store:
            self.append_to_order(key)
            return self.store[key]
        return -1 

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.store:
            self.append_to_order(key)
            self.store[key] = value
            return

        if key not in self.store:
            if self.size < self.capacity:
                self.size += 1
                self.append_to_order(key)
                self.store[key] = value
                return
            # need to nuke something here
            found = False
            while not found and self.order:
                # keep popping from order
                key_to_pop = self.order.pop(0)
                if key_to_pop in self.store:
                    found = True

            self.remove_from_cache(key_to_pop)
            self.append_to_order(key)
            self.store[key] = value
            self.size += 1

    @staticmethod
    def dedup(x, val):
        if x == val:
            return False
        return True 

    def remove_from_cache(self, key):
        #self.order = [el for el in self.order if el!=key]
        if self.order:
            self.order.pop(0)
        self.store.pop(key)
        self.size -= 1

    def append_to_order(self, val):
        self.order = [el for el in self.order if el!=val]
        self.order.append(val)

    def show(self):
        print self.order
        for key, value in self.store.items():
            print key, value, ':::',
        print '\n'

# 2,[set(2,1),set(1,1),get(2),set(4,1),get(1),get(2)]
#[1,-1,1]

x = LRUCache(2)
x.set(2,1)
x.show()
x.set(1,1)
x.show()
print x.get(2)
x.show()
x.set(4,1)
x.show()
print x.get(1)
x.show()
print x.get(2)
x.show()

#for i in range(10):
#    x.set(i, i**2)
#    x.show()
