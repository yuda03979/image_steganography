class BinaryHeap:

    def __init__(self):
        self._heap = []

    def enqueue(self, node):
        """
        Insert an item with its key into the heap and maintain the heap property.
        param: element = (key, item): tuple
        """
        self._heap.append(node)
        self._sift_up(len(self._heap))

    def dequeue(self):
        """
        Remove and return the item with the highest key from the heap, maintaining the heap property.
        ret: (key, data): tuple
        """
        if self.isEmpty():
            return None

        if len(self._heap) > 1:
            node, self._heap[0] = self._heap[0], self._heap.pop()
        else:
            node = self._heap.pop()

        self._sift_down(1)
        return node

    def peek(self):
        """
        Return the item with the highest key from the heap without removing it.
        """
        return self._heap[0] if not self.isEmpty() else None

    def isEmpty(self):
        """
        Check if the heap is empty and return True if it is, False otherwise.
        """
        return not self._heap

    def isNotEmpty(self):
        return not not self._heap

    def get_size(self):
        """
        Return the current number of items in the heap.
        """
        return len(self._heap)

    def build_heap(self, arr):
        """
        Build a heap from an array in O(N) time
        :param arr: list of HuffmanNode
        :return: None
        """
        if len(self._heap):
            return None
        self._heap = arr
        for i in range(self.get_size() // 2, -1, -1):
            self._sift_down(i)

    def change_priority(self, node, new_key):
        """
        Change the key of a specific item in the heap and adjust its position accordingly.
        """

        for i, j in enumerate(self._heap):
            if j[1] is node:
                node.key = new_key
                self._sift_down(i + 1)
                self._sift_up(i + 1)

    def _sift_up(self, i: int):
        """
        Move the element at index i upwards in the heap until it reaches its proper position.
        param: i = len(arr)
        """
        parent = i // 2
        while parent > 0:
            if self._heap[parent - 1] > self._heap[i - 1]:
                self._heap[parent - 1], self._heap[i - 1] = self._heap[i - 1], self._heap[parent - 1]
                i = parent
                parent = i // 2
                continue
            break

    def _sift_down(self, index):
        """
        Move the element at index i downwards in the heap until it reaches its proper position.
        param: i = len(arr) עד ועד בכלל
        """
        heap_size = len(self._heap) - 1

        while True:

            left = 2 * index
            right = (2 * index) + 1

            largest = index
            if left <= heap_size and self._heap[left - 1] < self._heap[index - 1]:
                largest = left
            if right <= heap_size and self._heap[right - 1] < self._heap[largest - 1]:
                largest = right

            if largest != index:
                self._heap[index - 1], self._heap[largest - 1] = self._heap[largest - 1], self._heap[index - 1]
                index = largest
                continue
            break


class BinaryHeapNode:

    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __lt__(self, other):
        return True if self.key < other.key else False

    def __le__(self, other):
        return True if self.key <= other.key else False

    def __eq__(self, other):
        return True if self.key == other.key else False

    def __ge__(self, other):
        return True if self.key >= other.key else False

    def __gt__(self, other):
        return True if self.key > other.key else False