# File: simple_queue.py

# IMPORTANT: Do not modify the following class in any way!

class SimpleQueue:

    def __init__(self):
        self._info = []

    def insert(self, x):
        self._info.append(x)
        return self

    def remove(self):
        if self.is_empty():
            raise RuntimeError("Can't remove if queue is empty")
        else:
            return self._info.pop(0)

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self._info)

    def __repr__(self):
        return repr(self._info)
