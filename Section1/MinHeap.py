class MinHeap:
    def __init__(self):
        self.min_heap = []

    def add(self, value):
        self.min_heap.append(value)
        self._bubble_up(len(self.min_heap) - 1)

    def _bubble_up(self, index):
        if index > 0:
            parent = self._get_parent(index)
            if self.min_heap[index] < self.min_heap[parent]:
                self._swap(index, parent)
                self._bubble_up(parent)

    def query(self):
        return self.min_heap[0]

    def extract(self):
        result = self.query()
        self.min_heap[0] = self.min_heap[len(self.min_heap) - 1]
        del self.min_heap[len(self.min_heap) - 1]
        self._heapify(0)
        return result

    def _heapify(self, index):
        index_left = self._get_left(index)
        index_right = self._get_right(index)
        if index_left >= len(self.min_heap):
            return
        if index_right >= len(self.min_heap):
            index_child = index_left
        else:
            index_child = index_right if self.min_heap[index_right] < self.min_heap[index_left] else index_left
        if self.min_heap[index_child] < self.min_heap[index]:
            self._swap(index, index_child)
            self._heapify(index_child)

    def _swap(self, index1, index2):
        self.min_heap[index1], self.min_heap[index2] = self.min_heap[index2], self.min_heap[index1]

    def _get_left(self, index):
        return (index + 1) * 2 - 1

    def _get_right(self, index):
        return self._get_left(index) + 1

    def _get_parent(self, index):
        return index // 2
