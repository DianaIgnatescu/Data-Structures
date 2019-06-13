class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        pass

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

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
        pass
