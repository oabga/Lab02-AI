import heapq

class PriorityQueue:
    def __init__(self, items=(), key=lambda x:x):
        self.key = key
        self.items = []
        for item in items:
            self.add(item)

    def add(self, item):
        # (cost, node) # node:'0'

        pair = (self.key(item), item)
        heapq.heappush(self.items, pair)

    def pop(self):
        return heapq.heappop(self.items)[1]