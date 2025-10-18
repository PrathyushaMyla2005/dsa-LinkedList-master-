
# insert at beginning of linked list
# Step 1: Define the Node class
class Node:
    def __init__(self, data):
        self.data = data      # store the data value
        self.next = None      # initially, no next node


# Step 2: Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None      # initially, list is empty

    # Step 3: Function to insert at beginning
    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)   # create a new node with given data
        new_node.next = self.head   # make new node point to current head
        self.head = new_node        # move head to point to new node

    # Step 4: Function to print the list
    def print_list(self):
        temp = self.head # traverse the list
        while temp:# print each node's data
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")  # end of the list indicator


# Step 5: Create a linked list and insert nodes
ll = LinkedList()          # start with an empty list
ll.insert_at_beginning(30) # List: 30 → None
ll.insert_at_beginning(20) # List: 20 → 30 → None
ll.insert_at_beginning(10) # List: 10 → 20 → 30 → None

# Step 6: Print the final list
ll.print_list()
#insert at end
# Step 1: Define the Node class
class Node:
    def __init__(self, data):
        self.data = data      # store the data value
        self.next = None      # initially, no next node
# Step 2: Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None      # initially, list is empty
    # Step 3: Function to insert at end
    def insert_at_end(self, new_data):
        new_node = Node(new_data)   # create a new node with given data
        if self.head is None:       # if list is empty, new node becomes head
            self.head = new_node # if first node, make it head
            return
        last = self.head          # start from head
        while last.next:            # traverse to the last node
            last = last.next # move to next node
        last.next = new_node        # make last node point to new node
    # Step 4: Function to print the list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")  # end of the list indicator
# Step 5: Create a linked list and insert nodes
ll = LinkedList()          # start with an empty list
ll.insert_at_end(10)      # List: 10 → None
ll.insert_at_end(20)      # List: 10 → 20 → None
ll.insert_at_end(30)      # List: 10 → 20 → 30 → None
# Step 6: Print the final list
ll.print_list()
#insert at specific position
# Step 1: Define a Node class
class Node:
    def __init__(self, data):
        self.data = data       # store the value
        self.next = None       # pointer to next node (None initially)

# Step 2: Define a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None       # head points to the first node

    # Step 3: Function to insert at a specific position
    def insert_at_position(self, position, new_data):
        new_node = Node(new_data)   # create a new node with the given value

        # Case 1: Insert at the beginning (position 0)
        if position == 0:
            new_node.next = self.head  # new node points to current head
            self.head = new_node       # head is now the new node
            return

        # Case 2: Insert at position > 0
        current = self.head             # start from the first node
        # Move to the node just before the desired position
        for _ in range(position - 1):
            if current is None:        # if position is out of bounds
                print("Position out of bounds")
                return
            current = current.next

        # Insert the new node
        new_node.next = current.next if current else None  # new node points to next node
        if current:
            current.next = new_node    # previous node points to new node

    # Step 4: Function to print the linked list
    def print_list(self):
        temp = self.head               # start from head
        while temp:                    # loop until end of list
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")                  # end of list

# ---------------- Example Usage ---------------- #

# Create an empty linked list
ll = LinkedList()

# Add initial nodes manually
ll.insert_at_position(0, 10)  # List: 10
ll.insert_at_position(1, 20)  # List: 10 → 20
ll.insert_at_position(2, 30)  # List: 10 → 20 → 30

print("Original list:")
ll.print_list()                 # Output: 10 → 20 → 30 → None

# Insert 15 at position 1 (between 10 and 20)
ll.insert_at_position(1, 15)

print("After inserting 15 at position 1:")
ll.print_list()                 # Output: 10 → 15 → 20 → 30 → None

# Insert 5 at position 0 (at the beginning)
ll.insert_at_position(0, 5)

print("After inserting 5 at position 0:")
ll.print_list()                 # Output: 5 → 10 → 15 → 20 → 30 → None

# Insert 35 at position 5 (at the end)
ll.insert_at_position(5, 35)

print("After inserting 35 at position 5:")
ll.print_list()                 # Output: 5 → 10 → 15 → 20 → 30 → 35 → None
