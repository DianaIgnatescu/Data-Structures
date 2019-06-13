"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if not self.length:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head.insert_before(value)
            new_node = self.head.prev
            self.head = new_node
            self.length += 1

    def remove_from_head(self):
        removed_head = self.head.value
        if self.length == 1:
            self.head.delete()
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.head = self.head.next
            self.head.prev.delete()
            self.length -= 1
        return removed_head

    def add_to_tail(self, value):

        if not self.length:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.insert_after(value)
            new_node = self.tail.next
            self.tail = new_node
            self.length += 1

    def remove_from_tail(self):

        removed_tail = self.tail.value
        if self.length == 1:
            self.tail.delete()
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.tail = self.tail.prev
            self.tail.next.delete()
            self.length -= 1
        return removed_tail

    def move_to_front(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            front_node = node
            node.delete()
            front_node.prev = None
            front_node.next = self.head
            self.head = front_node

    def move_to_end(self, node):
        if self.tail is not node:
            if node.next and node.prev:
                node.prev.next = node.next
                node.next.prev = node.prev

            elif node.next:
                node.next.prev = None

            if self.length > 1:
                self.head = self.tail

            end_node = self.tail
            self.tail = node
            node.prev = end_node
            end_node.next = node


  def delete(self, node):
    pass
    
  def get_max(self):
    pass
