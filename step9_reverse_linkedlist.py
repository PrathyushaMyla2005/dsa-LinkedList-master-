# -------------------------------
# Node class represents a single node in the linked list
# -------------------------------
class Node:
    def __init__(self, data):
        self.data = data      # store the value/data of the node
        self.next = None      # 'next' pointer initially None (no next node yet)


# -------------------------------
# LinkedList class to manage the linked list
# -------------------------------
class LinkedList:
    def __init__(self):
        self.head = None      # initially, the list is empty → head points to None

    # -------------------------------
    # Function to add a new node at the end of the list
    # -------------------------------
    def insert_at_end(self, data):
        new_node = Node(data)           # Step 1: create a new node with given data
        if self.head is None:           # Step 2: if list is empty
            self.head = new_node        # → make the new node the head of the list
            return
        temp = self.head                # Step 3: use temp to traverse the list
        while temp.next:                # Step 4: move temp until it reaches the last node
            temp = temp.next
        temp.next = new_node            # Step 5: link last node's next to the new node

    # -------------------------------
    # Function to reverse the linked list using a stack
    # -------------------------------
    def reverse_using_stack(self):
        if self.head is None:           # Step 0: if the list is empty, nothing to reverse
            return

        stack = []                      # Step 1: create an empty stack to store nodes
        temp = self.head                # Step 2: temp pointer to traverse the list

        # Step 3: Push all nodes of the linked list into the stack
        while temp:
            stack.append(temp)          # → push current node into the stack
            temp = temp.next            # → move temp to the next node

        # Step 4: Pop the first node from stack → this becomes the new head
        self.head = stack.pop()         # head now points to the last node of original list
        temp = self.head                # temp will help in connecting remaining nodes

        # Step 5: Pop remaining nodes and reconnect them in reverse order
        while stack:
            popped_node = stack.pop()   # get the next node from stack
            temp.next = popped_node     # connect it after the current node
            temp = temp.next            # move temp to this newly connected node

        # Step 6: After all nodes are connected, last node should point to None
        temp.next = None

    # -------------------------------
    # Function to print the linked list
    # -------------------------------
    def print_list(self):
        temp = self.head                # start from head
        while temp:                      # traverse until the end
            print(temp.data, end=" → ") # print node data
            temp = temp.next            # move to next node
        print("None")                   # indicate end of the list
ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)

print("Original List:")
ll.print_list()

ll.reverse_using_stack()

print("Reversed List:")
ll.print_list()
#recurvise
# -------------------------------
# Node class represents a single node in the linked list
# -------------------------------
class Node:
    def __init__(self, data):
        self.data = data      # store the value/data of the node
        self.next = None      # pointer to the next node, initially None


# -------------------------------
# LinkedList class to manage the list
# -------------------------------
class LinkedList:
    def __init__(self):
        self.head = None      # head points to the first node, initially list is empty

    # -------------------------------
    # Function to add a new node at the end of the list
    # -------------------------------
    def insert_at_end(self, data):
        new_node = Node(data)           # Step 1: create a new node with given data
        if not self.head:               # Step 2: check if the list is empty
            self.head = new_node        # → if empty, new node becomes the head
            return                      # exit the function
        temp = self.head                # Step 3: temp pointer to traverse the list
        while temp.next:                # Step 4: move temp until last node (where next is None)
            temp = temp.next
        temp.next = new_node            # Step 5: link the last node to the new node

    # -------------------------------
    # Recursive function to reverse the linked list
    # -------------------------------
    def reverse_recursive(self, head):
        # Step 1: Base case
        # If the list is empty (head is None) or only one node, return head
        if head is None or head.next is None:
            return head

        # Step 2: Recursively reverse the rest of the list
        # This call will reverse all nodes after the current head
        new_head = self.reverse_recursive(head.next)

        # Step 3: Reverse the link
        # head.next points to the next node
        # We want that node's next to point back to head
        head.next.next = head

        # Step 4: Current node becomes new tail, so its next should be None
        head.next = None

        # Step 5: Return new head of the reversed list
        return new_head

    # -------------------------------
    # Helper function to start reversal from the head
    # -------------------------------
    def reverse(self):
        # call recursive function starting from head and update head
        self.head = self.reverse_recursive(self.head)

    # -------------------------------
    # Function to print linked list
    # -------------------------------
    def print_list(self):
        temp = self.head                # start from head
        while temp:                      # traverse until end of list
            print(temp.data, end=" → ") # print current node data
            temp = temp.next            # move to next node
        print("None")                   # indicate end of list
ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)

print("Original List:")
ll.print_list()

ll.reverse()  # recursive reversal

print("Reversed List:")
ll.print_list()
