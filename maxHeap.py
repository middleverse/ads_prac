# ========
# Max Heap
# ========

class MaxHeap:
    def __init__(self, items=[]):
        """ Initialize heap """
        self.heap = [0]
        # append all items passed in, if any
        for i in items:
            self.heap.append(i)
            # float items up to their proper position
            self.__floatUp(len(self.heap) - 1)  

    def push(self, data):
        """ Push an item onto the heap """        
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        """ Check to see if heap is empty
            Return the first value if not
            Return False if empty
        """
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    
    def pop(self):
        """ Remove the max (first) element and return the new max
            3 Possibilities:
            - Empty Heap (return Flase)
            - Heap of size 1 (pop off the top value)
            - Heap of size more than 1 (pop off the top value and find new top)
        """
        # more than 2 elements
        if len(self.heap) > 2: 
            # swap first and last value of the heap
            self.__swap(1, len(self.heap) - 1)
            # pop the max value off the heap
            max = self.heap.pop()
            # bubble down the value in position 1 to 
            # its proper position
            self.__bubbleDown(1) 

        # 1 element    
        elif len(self.heap) == 2: 
            max = self.heap.pop()
        
        # no elements
        else: 
            max = False
        return max
    
    def __swap(self, i, j):
        """ Swap element in index i with element in index j """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def __floatUp(self, index):
        """ Float up element at index to its proper position """
        parent = index // 2
        # if we're passed the element at index 1, return
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)
    
    def __bubbleDown(self, index):
        """ (Also known as Max Heapify) 
            Bubble down the value at index to its proper position
        """
        # define left and right children indexes
        left = index * 2
        right = left + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest) # NOTE: value swap, not index
            self.__bubbleDown(largest) 

m = MaxHeap([95, 3, 21])
print(*m.heap)
m.push(10)
m.push(0)

for i in range(len(m.heap)):
    print('Popped: %s' % (m.pop()))
    print(m.heap)