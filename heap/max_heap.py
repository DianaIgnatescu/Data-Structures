class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        return self._bubble_up(len(self.storage) - 1)

    def delete(self):
        deleted = self.storage[0]
        self.storage[0] = self.storage[-1]
        self.storage.pop()
        self._sift_down(0)
        return deleted

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # in worst case element will need to make way to top of heap
        while index> 0:
            # get parent element of this index
            parent = (index - 1) // 2

            # check if the element at the index is higher priority than parent element
            if self.storage[index] > self.storage[parent]:
                # if it is then swap them
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

                # update index to be new spot that swapped element now resides at
                index = parent

            else:
                # otherwise our element is at a valid spot in the heap
                # we no longer need to bubble up
                break

    def _sift_down(self, index):
        last_index = len(self.storage) - 1
        while index * 2 + 1 <= last_index:
            left_child_index = index * 2 + 1
            right_child_index = index * 2 + 2
            if right_child_index > last_index:
                largest_index = left_child_index
            else:
                if self.storage[left_child_index] > self.storage[right_child_index]:
                    largest_index = left_child_index
                else:
                    largest_index = right_child_index

            if self.storage[index] < self.storage[largest_index]:
                self.storage[index], self.storage[largest_index] = self.storage[largest_index], self.storage[index]
            index = largest_index
