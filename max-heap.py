class MaxHeap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [0] * self.capacity
        self.heap_size = 0

    def parent(self, index):
        return index // 2

    def left(self, index):
        return 2 * index

    def right(self, index):
        return 2 * index + 1

    def max_heapify(self, index):
        left = self.left(index)
        right = self.right(index)
        if left <= self.heap_size and self.array[left] > self.array[index]:
            largest = left
        else:
            largest = index
        if right <= self.heap_size and self.array[right] > self.array[largest]:
            largest = right
        if largest != index:
            self.swap(index, largest)
            self.max_heapify(largest)

    def build_max_heap(self):
        for i in range(self.heap_size // 2, -1, -1):
            self.max_heapify(i)

    def swap(self, i, j):
        tmp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = tmp

    def insert(self, data):
        self.array[self.heap_size] = data
        self.heap_size += 1
        self.build_max_heap()


if __name__ == "__main__":
    heap = MaxHeap()

    heap.insert(5)
    heap.insert(12)
    heap.insert(64)
    heap.insert(1)
    heap.insert(37)
    heap.insert(90)
    heap.insert(91)
    heap.insert(97)

    print(heap.array)

    # [97, 91, 37, 90, 5, 12, 1, 64, 0, 0]
    """
                 97
               /    \
              91    37
             / \    / \
            90 5  12  1
           /
          64 
    """

