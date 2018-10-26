# a minheap used for store the 10 most commonly appeared job and state

class MinHeap:
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.heap_value = [None] * maxsize
        self.heap_key = [None] * maxsize
        self.count = 0

    #add job/state to the heap if their count is larger than the minimum count in the heap.
    def add(self, key, value):
        if self.count < self.maxsize:
            self.heap_value[self.count] = value
            self.heap_key[self.count] = key
            self.count = self.count + 1
            self.percolate_up(self.count-1)
        elif self.count == self.maxsize and value > self.heap_value[0]:
            self.heap_value[0] = value
            self.heap_key[0] = key
            self.percolate_down(0)

    #maintain heap property
    def percolate_up(self, index):
        if index > 0:
            parent = int((index-1)/2)
            if self.heap_value[index] < self.heap_value[parent]:
                tmp_value = self.heap_value[index]
                tmp_key = self.heap_key[index]
                self.heap_value[index] = self.heap_value[parent]
                self.heap_key[index] = self.heap_key[parent]
                self.heap_value[parent] = tmp_value
                self.heap_key[parent] = tmp_key
                self.percolate_up(parent)

    #return the minimum count in the heap
    def extract(self):
        value = self.heap_value[0]
        key = self.heap_key[0]
        self.count = self.count - 1
        self.heap_value[0] = self.heap_value[self.count]
        self.heap_key[0] = self.heap_key[self.count]
        self.percolate_down(0)
        return key,value

    #maintain heap property
    def percolate_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        if (left < self.count and right < self.count and
            self.heap_value[left] <= self.heap_value[index] and
            self.heap_value[left] <= self.heap_value[right]):
            self.heap_value[index],self.heap_value[left] = self.heap_value[left],self.heap_value[index]
            self.heap_key[index],self.heap_key[left] = self.heap_key[left],self.heap_key[index]
            self.percolate_down(left)
        elif (right < self.count and left < self.count and
            self.heap_value[right] <= self.heap_value[index] and
            self.heap_value[right] <= self.heap_value[left]):
            self.heap_value[index],self.heap_value[right] = self.heap_value[right],self.heap_value[index]
            self.heap_key[index],self.heap_key[right] = self.heap_key[right],self.heap_key[index]
            self.percolate_down(right)
        elif (left < self.count and right >= self.count and
              self.heap_value[left] <= self.heap_value[index]):
            self.heap_value[index],self.heap_value[left] = self.heap_value[left],self.heap_value[index]
            self.heap_key[index],self.heap_key[left] = self.heap_key[left],self.heap_key[index]
            self.percolate_down(left)
