from collections import deque
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = deque()
        while iterator.hasNext():
            self.iterator.append(iterator.next())
    def peek(self):
        return self.iterator[0]
    def next(self):
        return self.iterator.popleft()
    def hasNext(self):
        return len(self.iterator)>0
