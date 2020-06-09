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

    def __str__(self):
        print(f"Head: {self.head}, Tail: {self.tail}")

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):

        # create a new_node
        new_node = ListNode(value, None, None)

        # check if the DLL is empty (is there a head?)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if not self.head:
            return None
        elif self.length == 1:
            old_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return old_head.value
        else:
            old_head = self.head
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head
            self.length -= 1
            return old_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # create a new node
        new_node = ListNode(value, None, None)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if self.length > 1:
            old_tail = self.tail
            new_tail = self.tail.prev
            self.tail.prev = None
            self.tail = new_tail
            self.length -= 1
            return old_tail.value
        elif self.length == 1:
            old_tail = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return old_tail.value
        else:
            return None

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        elif node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            next_node = node.next
            prev_node = node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        if self.length > 0:
            max_value = self.head.value
            current = self.head
            while current.next != None:
                if current.value > max_value:
                    max_value = current.value
                current = current.next
            if max_value > current.value:
                return max_value
            else:
                return current.value
        else:
            return None
