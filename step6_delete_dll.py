# -----------------------------------
# Step 1: Define the Node class
# -----------------------------------
class Node:
    def __init__(self, data):
        # Each node stores three things:
        # 1️⃣ data → the actual value in the node
        # 2️⃣ prev → pointer to the previous node (None initially)
        # 3️⃣ next → pointer to the next node (None initially)
        self.data = data
        self.prev = None
        self.next = None


# -----------------------------------
# Step 2: Define the DoublyLinkedList class
# -----------------------------------
class DoublyLinkedList:
    def __init__(self):
        # head stores the address of the first node in the list
        # Initially, the list is empty → so head = None
        self.head = None


    # -----------------------------------
    # INSERT a node at the END of DLL
    # -----------------------------------
    def insert_at_end(self, data):
        # Step 1: Create a new node
        new_node = Node(data)

        # Step 2: If list is empty, new node becomes the head
        if self.head is None:
            self.head = new_node
            return  # stop here (no need to continue)

        # Step 3: Otherwise, move to the last node
        temp = self.head
        while temp.next:
            temp = temp.next  # move forward until next is None

        # Step 4: Connect the new node at the end
        temp.next = new_node     # last node's next → new node
        new_node.prev = temp     # new node's prev → last node


    # -----------------------------------
    # DELETE node at the BEGINNING
    # -----------------------------------
    def delete_at_beginning(self):
        # Step 1: If list is empty, nothing to delete
        if self.head is None:
            print("List is empty, nothing to delete.")
            return

        # Step 2: Store current head node temporarily
        temp = self.head

        # Step 3: Move head to the next node
        self.head = self.head.next

        # Step 4: If list still has nodes after deletion,
        # make new head’s prev pointer None
        if self.head is not None:
            self.head.prev = None

        # Step 5: Delete the old head node to free memory
        del temp


    # -----------------------------------
    # DELETE node at the END
    # -----------------------------------
    def delete_at_end(self):
        # Step 1: If list is empty
        if self.head is None:
            print("List is empty, nothing to delete.")
            return

        # Step 2: If only one node exists
        if self.head.next is None:
            temp = self.head     # store the only node
            self.head = None     # list becomes empty
            del temp             # delete the node
            return

        # Step 3: Move to the last node
        temp = self.head
        while temp.next:
            temp = temp.next

        # Step 4: Disconnect last node from the list
        temp.prev.next = None  # second-last node's next becomes None

        # Step 5: Delete the last node
        del temp


    # -----------------------------------
    # DELETE node at a SPECIFIC POSITION
    # -----------------------------------
    def delete_at_position(self, pos):
        # Step 1: If list is empty
        if self.head is None:
            print("List is empty, nothing to delete.")
            return

        # Step 2: If deleting the first node
        if pos == 1:
            self.delete_at_beginning()
            return

        # Step 3: Move to the node at given position
        temp = self.head
        count = 1
        while temp is not None and count < pos:
            temp = temp.next
            count += 1

        # Step 4: If position is invalid (out of range)
        if temp is None:
            print("Position out of range")
            return

        # Step 5: If node to delete has a next node,
        # connect next node's prev to current node's prev
        if temp.next:
            temp.next.prev = temp.prev

        # Step 6: If node to delete has a previous node,
        # connect previous node's next to current node's next
        if temp.prev:
            temp.prev.next = temp.next

        # Step 7: Finally, delete the node
        del temp


    # -----------------------------------
    # DISPLAY the entire DLL
    # -----------------------------------
    def display(self):
        temp = self.head  # start from head node
        while temp:
            print(temp.data, end=" ⇄ ")  # print each node's data
            temp = temp.next             # move forward
        print("None")  # represents end of list


# -----------------------------------
# Step 3: Example usage
# -----------------------------------
dll = DoublyLinkedList()  # create an empty doubly linked list

# Insert nodes at end → creates: 10 ⇄ 20 ⇄ 30 ⇄ 40
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_end(40)

print("Original list:")
dll.display()  # Output: 10 ⇄ 20 ⇄ 30 ⇄ 40 ⇄ None


# Delete node at beginning
dll.delete_at_beginning()
print("After deleting at beginning:")
dll.display()  # Output: 20 ⇄ 30 ⇄ 40 ⇄ None


# Delete node at end
dll.delete_at_end()
print("After deleting at end:")
dll.display()  # Output: 20 ⇄ 30 ⇄ None


# Delete node at position 2
dll.delete_at_position(2)
print("After deleting at position 2:")
dll.display()  # Output: 20 ⇄ None
