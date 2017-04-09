import heapq

class MinHeap:
    """Min heap class wrapping `heapq`."""

    def __init__(self, iterable=None):
        """Create a heap, optionally by copying elements from iterable."""
        self.heap = []
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push(self, item):
        """Push the value item onto this heap.

        >>> h = MinHeap([1,2,3])
        >>> h.push(0)
        """
        heapq.heappush(self.heap, item)

    def pop(self):
        """Pop the smallest item off this heap.

        >>> h = MinHeap([1,2,3])
        >>> h.pop()
        1
        """
        return heapq.heappop(self.heap)

    def replace(self, item):
        """Fast version of a pop followed by a push.

        >>> x = MinHeap([1,2,3])
        >>> x.replace(4)
        1
        """
        return heapq.heapreplace(self.heap, item)

    def pushpop(self, item):
        """Fast verion of a push followed by a pop.

        >>> x = MinHeap([1,2,3])
        >>> x.pushpop(0)
        0
        """
        return heapq.heappushpop(self.heap, item)

    def __str__(self):
        """
        >>> str(MinHeap())
        'MinHeap()'
        """
        return 'MinHeap({})'.format(', '.join(self.heap))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
