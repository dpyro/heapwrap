import heapq

class _ReverseHeapObject(object):
    """Wraps an object with reversed comparison operators."""

    @staticmethod
    def wrap_elements(iterable):
        """Wraps each element of iterable in place."""
        for i in range(iterable):
            iterable[i] = _ReverseHeapObject(iterable[i])

    @staticmethod
    def unwrap_elements(iterable):
        """Removes the wrapper from each element of iterable."""
        for i in range(iterable):
            assert isinstance(iterable[i], _ReverseHeapObject)

            iterable[i] = iterable[i].value

    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value
    def __gt__(self, other):
        return self.value < other.value
    def __eq__(self, other):
        return self.value == other.value
    def __str__(self):
        return 'ReverseHeapObject({})'.format(self.value)

class MaxHeap:
    """
    Max heap class wrapping `heapq`.

    Inspired by http://stackoverflow.com/a/40455775/1440740.
    """

    def __init__(self, iterable=None):
        """Create a heap, optionally by copying elements from iterable."""
        self.heap = []
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push(self, item):
        """Push the value item onto this heap.

        >>> h = MaxHeap([1,2,3])
        >>> h.push(4)
        """
        heapq.heappush(self.heap, _ReverseHeapObject(item))

    def pop(self):
        """Pop the largest item off this heap.

        >>> h = MaxHeap([1,2,3])
        >>> h.pop()
        3
        """
        return heapq.heappop(self.heap).value

    def replace(self, item):
        """Fast version of a pop followed by a push.

        >>> x = MaxHeap([1,2,3])
        >>> x.replace(4)
        3
        """
        wrapped_item = _ReverseHeapObject(item)
        return heapq.heapreplace(self.heap, wrapped_item).value

    def pushpop(self, item):
        """Fast verion of a push followed by a pop.

        >>> x = MaxHeap([1,2,3])
        >>> x.pushpop(0)
        3
        """
        wrapped_item = _ReverseHeapObject(item)
        return heapq.heappushpop(self.heap, wrapped_item).value

    def __len__(self):
        return self.heap.__len__()

    def __getitem__(self, key):
        if len(self.heap) > 0:
            return self.heap.__getitem__(key).value
        else:
            raise IndexError('heap index out of range')

    def __iter__(self):
        return self.heap.__iter__()

    def __reserved__(self):
        return self.heap.__reversed__()

    def __contains__(self, item):
        return self.heap.__contains__(_ReverseHeapObject(item))

    def __str__(self):
        """
        >>> str(MaxHeap())
        'MaxHeap()'
        """
        return 'MaxHeap({})'.format(', '.join(map(lambda x: x.value, self.heap)))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
