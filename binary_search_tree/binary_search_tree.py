class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Check new node val  < current nodes val
        if value < self.value:
            # if no left child place new node
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
            # otherwise repeat process
                self.left.insert(value)
            # check new node val >= current nodes val
        if value >= self.value:
            # if no right child place new node
            if not self.right:
                self.right = BinarySearchTree(value)
            # otherwise repeat process
            else:
                self.right.insert(value)

  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass