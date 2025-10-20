# Step 1: Define the Node class
class Node:
    def __init__(self, data):
        self.data = data    # store the data of the node
        self.next = None    # pointer to the next node (None initially)

# Step 2: Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None    # head initially points to None (empty list)

    # Function to delete the first node
    def delete_first(self):
        if not self.head:               # if the list is empty
            print("List is empty, nothing to delete.")
            return
        self.head = self.head.next      # move head to the second node
                                        # first node is now removed

    # Function to insert a node at the beginning (to test deletion)
    def insert_at_beginning(self, data):
        new_node = Node(data)           # create a new node
        new_node.next = self.head       # point new node to current head
        self.head = new_node            # update head to new node

    # Function to print the linked list
    def print_list(self):
        current = self.head
        while current:                  # traverse the list
            print(current.data, end=" -> ")
            current = current.next
        print("None")                   # end of the list
# Step 3: Create a linked list and test deletion
ll = LinkedList()
ll.insert_at_beginning(30)  # List: 30 -> None
ll.insert_at_beginning(20)  # List: 20 -> 30 -> None
ll.insert_at_beginning(10)  # List: 10 -> 20 -> 30 -> None
print("Original list:")
ll.print_list()              # Print the original list
ll.delete_first()           # Delete the first node
print("List after deleting the first node:")
ll.print_list()              # Print the list after deletion
#delete at end
# Step 1: Define the Node class
class Node:
    def __init__(self, data):
        self.data = data    # store the value of the node
        self.next = None    # pointer to the next node (None initially)

# Step 2: Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None    # head initially points to None (empty list)

    # Function to insert a node at the end (for testing)
    def append(self, data):
        new_node = Node(data)       # create a new node
        if not self.head:           # if the list is empty
            self.head = new_node    # new node becomes the head
            return
        current = self.head
        while current.next:         # traverse to the last node
            current = current.next
        current.next = new_node     # append the new node at the end

    # Function to delete the last node
    def delete_last(self):
        if not self.head:           # if the list is empty
            print("List is empty, nothing to delete.")
            return
        if not self.head.next:      # if there is only one node
            self.head = None        # remove it, list becomes empty
            return
        current = self.head
        while current.next.next:    # traverse to second-last node
            current = current.next
        current.next = None         # remove the last node

    # Function to print the linked list
    def print_list(self):
        current = self.head
        while current:              # traverse through the list
            print(current.data, end=" -> ")
            current = current.next
        print("None")               # end of the list
# Step 3: Create a linked list and test deletion
ll = LinkedList()
ll.append(10)               # List: 10 -> None
ll.append(20)               # List: 10 -> 20 -> None
ll.append(30)               # List: 10 -> 20 -> 30 -> None
print("Original list:")
ll.print_list()              # Print the original list
ll.delete_last()            # Delete the last node
print("List after deleting the last node:")
ll.print_list()              # Print the list after deletion
#delete specific position
# Step 1: Define the Node class
class Node:
    def __init__(self, data):
        self.data = data      # store the value of the node
        self.next = None      # pointer to the next node (None initially)
# Step 2: Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None      # head initially points to None (empty list)
    # Function to insert a node at the end (for testing)
    def append(self, data):
        new_node = Node(data)       # create a new node
        if not self.head:           # if the list is empty
            self.head = new_node    # new node becomes the head
            return
        current = self.head
        while current.next:         # traverse to the last node
            current = current.next
        current.next = new_node     # append the new node at the end
    # Function to delete a node at a specific position
    def delete_at_position(self, position):
        if not self.head:           # if the list is empty
            print("List is empty, nothing to delete.")
            return
        if position == 0:           # if head needs to be removed
            self.head = self.head.next
            return
        current = self.head
        prev = None
        count = 0
        while current and count < position:
            prev = current
            current = current.next
            count += 1
        if not current:             # if position is out of bounds
            print("Position out of bounds.")
            return
        prev.next = current.next     # unlink the node at the position
# Function to print the linked list
    def print_list(self):
        current = self.head
        while current:              # traverse through the list
            print(current.data, end=" -> ")
            current = current.next
        print("None")               # end of the list
# Step 3: Create a linked list and test deletion
ll = LinkedList()
ll.append(10)               # List: 10 -> None
ll.append(20)               # List: 10 -> 20 -> None
ll.append(30)               # List: 10 -> 20 -> 30 -> None
print("Original list:")
ll.print_list()              # Print the original list
ll.delete_at_position(1)    # Delete node at position 1
print("List after deleting node at position 1:")
ll.print_list()              # Print the list after deletion
ll.delete_at_position(0)    # Delete node at position 0
print("List after deleting node at position 0:")
ll.print_list()              # Print the list after deletion
ll.delete_at_position(5)    # Attempt to delete node at out-of-bounds position
print("List after attempting to delete node at out-of-bounds position:")
ll.print_list()              # Print the list after attempted deletion
