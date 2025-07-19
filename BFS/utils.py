import heapq

def euclidian_formula(A, B):
    return sum(abs(a - b)**2 for (a, b) in zip(A, B)) ** 0.5


class PriorityQueue:
    def __init__(self, items=(), key=lambda x : x):
        self.key = key
        self.items = []
        for item in items:
            self.add(item)

    def add(self, item):
        pair = (self.key(item), item)
        heapq.heappush(self.items, pair)

    def pop(self):
        return heapq.heappop(self.items)[1]