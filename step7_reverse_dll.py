# -----------------------------------
# Step 1: Define Node class
# -----------------------------------
class Node:
    def __init__(self, data):
        # 'data' stores the value of the node
        self.data = data
        # 'prev' points to previous node (None initially)
        self.prev = None
        # 'next' points to next node (None initially)
        self.next = None


# -----------------------------------
# Step 2: Define DoublyLinkedList class
# -----------------------------------
class DoublyLinkedList:
    def __init__(self):
        # 'head' points to the first node of the list
        self.head = None

    # -----------------------------
    # Insert a node at the END
    # -----------------------------
    def insert_at_end(self, data):
        # Step 1: Create a new node
        new_node = Node(data)

        # Step 2: If list is empty, make new node as head
        if self.head is None:
            self.head = new_node
            return  # stop here

        # Step 3: Traverse to the last node
        temp = self.head
        while temp.next:
            temp = temp.next  # move to next node until last

        # Step 4: Connect last node to new node
        temp.next = new_node     # last node's next → new node
        new_node.prev = temp     # new node's prev → last node

    # -----------------------------
    # Display the list
    # -----------------------------
    def display(self):
        temp = self.head  # start from head
        while temp:
            print(temp.data, end=" ⇄ ")  # print node data
            temp = temp.next             # move forward
        print("None")  # end of list

    # -----------------------------
    # Reverse the doubly linked list
    # -----------------------------
    def reverse(self):
        temp = None          # temporary variable to store previous node
        current = self.head  # start from the head node

        # Step 1: Traverse all nodes
        while current is not None:
            # Step 2: Swap prev and next for current node
            temp = current.prev        # store original prev
            current.prev = current.next  # swap prev → next
            current.next = temp          # swap next → prev

            # Step 3: Move to next node in original order
            # After swapping, original next is now prev
            current = current.prev

        # Step 4: Update head to new first node
        # 'temp' is at second node from end after loop, so move one back
        if temp is not None:
            self.head = temp.prev
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_end(40)

print("Original list:")
dll.display()  # Output: 10 ⇄ 20 ⇄ 30 ⇄ 40 ⇄ None

dll.reverse()  # Reverse the list

print("Reversed list:")
dll.display()  # Output: 40 ⇄ 30 ⇄ 20 ⇄ 10 ⇄ None
 