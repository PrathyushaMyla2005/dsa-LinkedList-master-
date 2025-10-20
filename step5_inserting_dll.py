# -----------------------------
# Step 1: Define a Node class
# -----------------------------
class Node:
    def __init__(self, data):
        # 'data' stores the actual value of the node
        self.data = data
        
        # 'prev' will point to the previous node (None initially)
        self.prev = None
        
        # 'next' will point to the next node (None initially)
        self.next = None


# -----------------------------
# Step 2: Define the Doubly Linked List (DLL) class
# -----------------------------
class DoublyLinkedList:
    def __init__(self):
        # 'head' stores the first node of the list
        # Initially, the list is empty, so head = None
        self.head = None


    # -----------------------------
    # Insert a node at the BEGINNING
    # -----------------------------
    def insert_at_beginning(self, data):
        # Step 1: Create a new node with given data
        new_node = Node(data)

        # Step 2: Make new_node's next point to current head
        new_node.next = self.head

        # Step 3: If list is not empty,
        # make the current head's prev point back to new_node
        if self.head is not None:
            self.head.prev = new_node

        # Step 4: Move the head pointer to new_node
        # (new_node becomes the first node)
        self.head = new_node


    # -----------------------------
    # Insert a node at the END
    # -----------------------------
    def insert_at_end(self, data):
        # Step 1: Create a new node
        new_node = Node(data)

        # Step 2: If list is empty, new_node becomes head
        if self.head is None:
            self.head = new_node
            return  # stop function here

        # Step 3: Else, traverse to the last node
        temp = self.head
        while temp.next:
            temp = temp.next  # move forward until last node

        # Step 4: Link the last node with the new node
        temp.next = new_node     # last node's next → new_node
        new_node.prev = temp     # new_node's prev → last node


    # -----------------------------
    # Insert a node at a SPECIFIC POSITION
    # -----------------------------
    def insert_at_position(self, pos, data):
        # Case 1: If position is 1, just insert at beginning
        if pos == 1:
            self.insert_at_beginning(data)
            return

        # Step 1: Create a new node
        new_node = Node(data)

        # Step 2: Start from head and move to (pos-1)th node
        temp = self.head
        count = 1

        # Keep moving forward until you reach position-1
        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1

        # Step 3: If position is out of range (temp is None)
        if temp is None:
            print("Position out of range")
            return

        # Step 4: Adjust links for new_node
        # new_node's next should point to temp's next node
        new_node.next = temp.next

        # new_node's prev should point to temp
        new_node.prev = temp

        # Step 5: If not inserting at end,
        # make the next node’s prev point to new_node
        if temp.next:
            temp.next.prev = new_node

        # Step 6: Finally, connect temp’s next to new_node
        temp.next = new_node


    # -----------------------------
    # Display the entire DLL
    # -----------------------------
    def display(self):
        temp = self.head  # start from the head node

        # traverse until temp becomes None (end of list)
        while temp:
            print(temp.data, end=" ⇄ ")  # print node data
            temp = temp.next              # move to the next node

        print("None")  # shows end of the list


# -----------------------------
# Step 3: Example usage
# -----------------------------
dll = DoublyLinkedList()  # create an empty doubly linked list

# Insert nodes at end → creates list: 10 ⇄ 20 ⇄ 30
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)

# Insert at position 2 → inserts 15 between 10 and 20
# New list: 10 ⇄ 15 ⇄ 20 ⇄ 30
dll.insert_at_position(2, 15)

# Insert at beginning → adds 5 at start
# Final list: 5 ⇄ 10 ⇄ 15 ⇄ 20 ⇄ 30
dll.insert_at_beginning(5)

# Display the entire list
dll.display()
